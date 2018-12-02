from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import logging
import os

class EntityTypeClf():
    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.info("Initialisation of the EntityType Classifier.")
        
        print(os.getcwd())
        
        glove_vectors_file = "data/embedding_file/glove.840B.300d.txt"
        logger.info("Loading glove... (about 5 minutes)")
        self.glove_wordmap = {}
        with open(glove_vectors_file, "r", encoding = "utf-8") as glove:
            for line in glove:
                name, vector = tuple(line.split(" ", 1))
                self.glove_wordmap[name] = np.fromstring(vector, sep = " ")
        logger.info("GloVe is loaded.")
        
    def train(self, df):
        self.X, self.Y = self.construct_dataset(df)
        
        self.knn_clf = KNeighborsClassifier(n_neighbors = 3)
        self.knn_clf.fit(self.X, self.Y)
        
    def construct_dataset(self, dict_data):
        logger = logging.getLogger(__name__)
        
        X = []
        Y = []
        
        for entity in dict_data.keys():
            for value in dict_data[entity]:
                glove_word = value.replace(" ", "")
                try:
                    glove_representation = self.glove_wordmap[glove_word]
                except:
                    logger.info("Glove, error with the word: " + glove_word + ", no vectorial representation.")
                else:
                    X.append(glove_representation)
                    Y.append(entity)
                    
        return X, Y
    
    def predict_entity_type(self, value):
        logger = logging.getLogger(__name__)
        
        glove_word = value.replace(" ", "")
        try:
            glove_representation = self.glove_wordmap[glove_word]
        except:
            logger.info("Impossible to classify the value.")
            return ""
        else:
            return self.knn_clf.predict([glove_representation])[0]
