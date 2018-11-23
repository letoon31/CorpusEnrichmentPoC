from nltk.parse.stanford import StanfordDependencyParser

class IntentEntityExtractor():
    
    def __init__(self):
        self.path_to_jar = "data/dependency_parser/stanford-parser-full-2018-02-27/stanford-parser.jar"
        self.path_to_models_jar = "data/dependency_parser/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models.jar"
        
        self.dependency_parser = StanfordDependencyParser(path_to_jar = self.path_to_jar, path_to_models_jar = self.path_to_models_jar)
        
    def extract_intent(self, sentence):
        result = self.dependency_parser.raw_parse(sentence)
        dep = result.__next__()
        
        relations = list(dep.triples())
        
        intent = ""
        amod_intent = ""
        
        for relation in relations:
            if relation[1] == "nsubj":
                if relation[0][1] == "WP":
                    intent = relation[2][0].capitalize()
                    break
                elif relation[2][1] == "WP":
                    intent = relation[0][0].capitalize()
                    break
            
        for relation in relations:
            if relation[0][0] == intent.lower() and relation[1] == "amod":
                amod_intent = relation[2][0].capitalize()
        
        if amod_intent is not "":
            intent = amod_intent + " " + intent
        
        return intent
    
    def extract_entity_value(self, sentence, intent):
        result = self.dependency_parser.raw_parse(sentence)
        dep = result.__next__()
        
        relations = list(dep.triples())
        
        entity = ""
            
        for relation in relations:
            if relation[0][0] == intent.lower() and relation[1] == "nmod":
                entity = relation[2][0].capitalize()
            
        compound_entity = ""
        for relation in relations:
            if relation[0][0] == entity and relation[1] == "compound":
                compound_entity = relation[2][0].capitalize()
                
        if compound_entity is not "":
            entity = compound_entity + " " + entity
        
        return entity
        
    def extract_all(self, sentence):
        intent = self.extract_intent(sentence)
        entity_value = self.extract_entity_value(sentence, intent)
        
        return intent, entity_value
    
    def show_dependency_parsing(self, sentence):
        result = self.dependency_parser.raw_parse(sentence)
        dep = result.__next__()
        
        relations = list(dep.triples())
        
        for relation in relations:
            print(relation)
