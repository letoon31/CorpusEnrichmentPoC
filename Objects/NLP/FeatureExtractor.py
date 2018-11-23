import spacy
from benepar.spacy_plugin import BeneparComponent

class Feature_Extractor():
    def __init__(self):
        self.nlp = spacy.load("en")
        self.nlp.add_pipe(BeneparComponent("benepar_en"))
        
    def extract_feature(self, sentence, assistant):
        doc = self.nlp(sentence)
        sentence = list(doc.sents)[0]   
        pp = self.get_pp(sentence)
        
        print(pp)
        
        
    
    def get_pp(self, sentence):
        pp = []
        
        for ite in sentence._.constituents:
            if "PP" in ite._.labels:
                pp.append(ite)
                
        return pp
                
FE = Feature_Extractor()
FE.extract_feature("Who is the actor of Batman in TDK ?")