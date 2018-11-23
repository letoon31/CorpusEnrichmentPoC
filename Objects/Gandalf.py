from drqa import pipeline

class Gandalf(pipeline.DrQA):
    
    def __init__(self, tfidf_path = None, db_path = None):
        if tfidf_path:
            ranker_config = {
                'options': 
                {
                    'tfidf_path': tfidf_path
                }
            }
        else:
            ranker_config = None
            
        if db_path:
            db_config = {
                'options':
                {
                        'db_path': db_path
                }
            }
        else:
            db_config = None
                    
        pipeline.DrQA.__init__(self, cuda = False, ranker_config = ranker_config, db_config = db_config)
        
    def answer_question(self, question, top_n = 1, n_docs = 1):
        predictions = self.process(question, candidates = None, top_n = top_n, n_docs = n_docs, return_context = True)
        return predictions[0]["span"]
        
