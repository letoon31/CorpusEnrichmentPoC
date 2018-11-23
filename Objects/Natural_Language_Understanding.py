# we do the needed importations
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions, EntitiesOptions, SemanticRolesOptions

class NLU(NaturalLanguageUnderstandingV1):
    
    def __init__(self, username = '05a44a83-8ae6-4922-aef4-a0ee7651c635', password = 'tAnAk3kKY6oY'):
        NaturalLanguageUnderstandingV1.__init__(self,
            username= username,
            password=password,
            version='2018-03-16')
        
    def get_keywords(self, question):
        response = self.analyze(
            text = question,
            features = Features(
            keywords = KeywordsOptions()))
        
        keywords = []
        for i in range(0, 2):
            keywords.append(response["keywords"][i]["text"].lower())
        
        return keywords
    
    def return_entity(self, question, intent):
        keywords = self.get_keywords(question)
        keywords.remove(intent.lower())
        
        return keywords[0].capitalize()
    
    def return_intent(self, question, entity):
        keywords = self.get_keywords(question)
        keywords.remove(entity.lower())
        
        return keywords[0].capitalize()
    
    ##################
    ### DEPRECATED ###
    ##################
       
    def return_entities(self, question):
        response = self.analyze(
            text = question,
            features=Features(entities=EntitiesOptions()))
        
        print(json.dumps(response, indent=2))
    
    def return_semantic_roles(self, question):
        response = self.analyze(
            text=question,
            features=Features(
            semantic_roles=SemanticRolesOptions()))
        
        print(json.dumps(response, indent=2))
    