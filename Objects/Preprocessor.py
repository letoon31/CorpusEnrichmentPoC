import os
import json
import argparse
import math
import logging
from OpenDomainQA.scripts.retriever.build_db import store_contents
from OpenDomainQA.scripts.retriever.build_tfidf import get_count_matrix
from OpenDomainQA.scripts.retriever.build_tfidf import get_tfidf_matrix
from OpenDomainQA.scripts.retriever.build_tfidf import get_doc_freqs
from OpenDomainQA.drqa import retriever

class Preprocessor():
    def preprocess_dir(dir_path):
        if not os.path.isdir(dir_path):
            raise Exception("Wrong directory path")
        
        with open(dir_path + "/data.json", "w") as data_file:
            for file_path in os.listdir(dir_path):
                if file_path[-4:] == ".txt":
                    with open(dir_path + "/" + file_path, "r") as file:
                        dict_file = {}
                        
                        dict_file["id"] = file_path[:-4]
                        dict_file["text"] = file.read()
                        
                        json_file = json.dumps(dict_file)
                        
                        data_file.write(str(json_file) + "\n")
                        
        return dir_path + "/data.json"
    
    def buid_db(data_file, target_file):
        store_contents(data_file, target_file, None, None)
        
    def build_tfidf(db_path, out_dir):
        logger = logging.getLogger(__name__)
        
        parser = argparse.ArgumentParser(argument_default = argparse.SUPPRESS)
        parser.add_argument('db_path')
        parser.add_argument('out_dir')
        parser.add_argument('--ngram', type=int, default=2)
        parser.add_argument('--hash-size', type=int, default=int(math.pow(2, 24)))
        parser.add_argument('--tokenizer', type=str, default='simple')
        parser.add_argument('--num-workers', type=int, default=None)
        args = parser.parse_args([db_path, out_dir])
        
        logging.info('Counting words...')
        count_matrix, doc_dict = get_count_matrix(args, 'sqlite', {'db_path': args.db_path})
        
        logger.info('Making tfidf vectors...')
        tfidf = get_tfidf_matrix(count_matrix)
        
        logger.info('Getting word-doc frequencies...')
        freqs = get_doc_freqs(count_matrix)
        
        basename = os.path.splitext(os.path.basename(args.db_path))[0]
        basename += ('-tfidf-ngram=%d-hash=%d-tokenizer=%s' %
                 (args.ngram, args.hash_size, args.tokenizer))
        filename = os.path.join(args.out_dir, basename)

        logger.info('Saving to %s.npz' % filename)
        metadata = {
            'doc_freqs': freqs,
            'tokenizer': args.tokenizer,
            'hash_size': args.hash_size,
            'ngram': args.ngram,
            'doc_dict': doc_dict
        }
    
        retriever.utils.save_sparse_csr(filename, tfidf, metadata)
        
        return filename + ".npz"
    
    def preprocessing_data(dir_corpus):
        # create the JSON file
        data_file = Preprocessor.preprocess_dir(dir_corpus)
        
        # build the db file
        db_file = dir_corpus + "/db.db"
        Preprocessor.buid_db(data_file, db_file)
        
        # build the tfidf
        tfidf_file = Preprocessor.build_tfidf(db_file, dir_corpus)
        
        actual_path = os.getcwd()
        return actual_path + "/" + tfidf_file, actual_path + "/" + db_file