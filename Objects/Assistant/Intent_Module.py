import logging

class Intent_Module():
    
    def get_intent_list(self, nodejsconnector):
        response = nodejsconnector.list_intents()
        
        intents = []
        for intent in response["intents"]:
            intents.append(intent["intent"])
        
        return intents
    
    def get_examples_of_intent(self, nodejsconnector, intent):
        response_examples = nodejsconnector.list_examples(intent)
        
        return response_examples["examples"]
    
    def print_intents(self, nodejsconnector):
        logger = logging.getLogger(__name__)
        
        logger.info("We list the intents")
        intents = self.get_intent_list(nodejsconnector)
        logger.info("There is " + str(len(intents)) + " intents:" + str(intents))
        
    def print_intents_and_examples(self, nodejsconnector):
        logger = logging.getLogger(__name__)
        
        logger.info("We list every intents and examples for checking")

        intents = self.get_intent_list(nodejsconnector)

        for intent in intents:
            examples = self.get_examples_of_intent(nodejsconnector, intent)
            
            logger.info("Intent: " + intent + ", examples: " + str(examples))
            