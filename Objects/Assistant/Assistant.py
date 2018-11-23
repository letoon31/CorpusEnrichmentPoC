# importations about Watson Assistant
import logging
from Objects.Assistant.Workspace_Module import Workspace_Module
from Objects.Assistant.Intent_Module import Intent_Module
from Objects.Assistant.NodeJSConnector import NodeJSConnector

class Assistant():
    
    ######################
    ### INITIALISATION ###
    ######################
    
    def __init__(self, username = 'c964a8c0-3ba6-4c7b-9f03-cfb20ae9e99b', password = 'F0GxwsnQ3zUe', workspace_id = '', workspace_name = 'Superheroes Workspace', remove_workspaces = False):
        logger = logging.getLogger(__name__)
        
        logger.info("Configuration of Watson Assistant.")
        self.nodejsconnector = NodeJSConnector(username, password)
        
        # Initialisation of modules
        self.workspace_module = Workspace_Module()
        self.intent_module = Intent_Module()
        
        if remove_workspaces:
            logger.info("We are removing all the workspaces.")
            self.remove_all_workspaces()
        
        if workspace_id != "":
            self.workspace_id = workspace_id
        elif workspace_name != "":
            self.create_new_workspace(workspace_name)
            self.nodejsconnector.set_workspace_id(self.retrieve_workspace_id(workspace_name))
        else:
            raise Exception("No Workspace ID or Name: Initialisation Error.")
        
        self.intents = []
        self.entities = []
        
        
    ##################
    ### WORKSPACES ###
    ##################
    
    # to get the worspace list
    def get_workspace_list(self):
        return self.workspace_module.get_workspace_list(self.nodejsconnector)
        
    # function creating a new workspace, if the workspace already exist, nothing is done
    def create_new_workspace(self, workspace_name, workspace_description = 'A new workspace'):
        return self.workspace_module.create_new_workspace(self.nodejsconnector, workspace_name, workspace_description)
    
    # remove a workspace
    def remove_workspace(self, workspace_id = ""):
        return self.workspace_module.remove_workspace(self.nodejsconnector, workspace_id)
                
    # function returning the id of the workspace
    def retrieve_workspace_id(self, workspace_name):
        return self.workspace_module.retrieve_workspace_id(self.nodejsconnector, workspace_name)
    
    # remove all workspaces
    def remove_all_workspaces(self):
        self.workspace_module.remove_all_workspaces(self.nodejsconnector)
    
    
    ###############
    ### INTENTS ###
    ###############    
    
    # get the intents of our workspace
    def get_intents_list(self):
        return self.intent_module.get_intent_list(self.nodejsconnector)
    
    def get_examples_of_intent(self, intent):
        return self.intent_module.get_examples_of_intent(self.nodejsconnector, intent)
    
    def upload_list_intents(self):
        self.intents = self.get_intents_list()
    
    # print the existing intents of our workspace
    def print_intents(self):
        self.upload_list_intents()
        self.intent_module.print_intents(self.nodejsconnector)
        
    def print_intents_and_examples(self):
        self.upload_list_intents()
        self.intent_module.print_intents_and_examples(self.nodejsconnector)
            
#    def show_intents_and_examples(self):
#        self.upload_list_intents()
#
#        for intent in self.intents:
#            examples = self.get_examples_of_intent(intent)
#            
#            print("Intent: " + intent + ", examples: " + str(examples))
        
    def create_new_intent(self, name):
        logger = logging.getLogger(__name__)
        
        logger.info("Creation of the intent: " + name)
        self.nodejsconnector.create_intent(name)
    
    # add intent to the workspace
    def create_intent_to_workspace(self, name):
        logger = logging.getLogger(__name__)
        
        logger.info("Checking if the intent already exist")
        name = name.replace(" ", "_")
        if name in self.intents:
            logger.info("Already exists")
            return
    
        logger.info("Doen't exist")
        self.create_new_intent(name)
        
        
    ################
    ### ENTITIES ###
    ################
    
    def get_entities_list(self):
        response = self.nodejsconnector.list_entities()
        
        entities = []
        for entity in response["entities"]:
            entities.append(entity["entity"])
        
        return entities
    
    def get_values_of_entity(self, entity):
        response = self.nodejsconnector.list_values(entity)
        
        values = []
        for value in response["values"]:
            values.append(value["value"])
        
        return values
    
    def upload_list_entities(self):
        list_entities = []

        list_entities_res = self.get_entities_list()

        for entity in list_entities_res:
            list_entities.append(entity)
            
        self.entities = list_entities
        
    def print_entities(self):
        logger = logging.getLogger(__name__)
        
        logger.info("We list the entities")
        self.upload_list_entities()
        logger.info("There is " + str(len(self.entities)) + " entities: " + str(self.entities))
        
    def print_entities_and_values(self):
        logger = logging.getLogger(__name__)
        
        logger.info("We list every entities and values for checking")
        self.upload_list_entities()

        for entity in self.entities:
            values = self.get_values_of_entity(entity)
    
            logger.info(entity + ", values: " + str(values))
            
    def show_entities_and_values(self):
        self.upload_list_entities()

        for entity in self.entities:
            values = self.get_values_of_entity(entity)
    
            print(entity + ", values: " + str(values))
        
    def create_new_entity(self, name):
        logger = logging.getLogger(__name__)
        
        name = name.replace(" ", "")
        logger.info("Creation of the entity: " + name)
        self.nodejsconnector.create_entity(name)
        
    def create_value_to_entity(self, entity, value):
        logger = logging.getLogger(__name__)
        
        entity = entity.replace(" ", "")
        logger.info("Adding the element: " + value + " to entity " + entity)
        self.nodejsconnector.create_value(entity, value)
        
    def create_entity_to_workspace(self, name, values):
        logger = logging.getLogger(__name__)
        
        name = name.replace(" ", "")
        
        logger.info("Checking if existing")
        self.upload_list_entities()
        if name in self.entities:
            logger.info("Exists")
        else:
            logger.info("Doesn't exist.")
            self.create_new_entity(name)
    
        logger.info("We add values for this entity.")
        existed_values = self.get_values_of_entity(name)
        for value in values:
            logger.info("We are checking if the value " + value + " already exists for this entity.")
            if value not in existed_values:
                logger.info("This value does not exist for this entity.")
                self.create_value_to_entity(name, value)
            else:
                logger.info("This value already exists.")
            
    def create_system_entities(self, system_entities):
        logger = logging.getLogger(__name__)
        
        self.upload_list_entities()
        for entity in system_entities:
            logger.info("For: " + entity)
            self.create_entity_to_workspace(entity, [])
            
    def send_question(self, question):
        logger = logging.getLogger(__name__)
        
        logger.info("We send this question to the Assistant: " + question)
        response = self.nodejsconnector.message(question)
        logger.info("The question is sent")
    
        return response
    
    def extract_intent(self, response):
        logger = logging.getLogger(__name__)
        
        logger.info("Intent extraction")
        #If intents are detected, we take the one with the best confidence

        if response["intents"]:
            intent = response["intents"][0]['intent']
            confidence_rate = response["intents"][0]['confidence']
            logger.info("There is intent " + intent + " with confidence " + str(confidence_rate))
        
            if len(response["intents"]) > 1:
                for i in range(1, len(response["intents"])):
                    new_intent = response["intents"][i]["intent"]
                    new_confidence_rate = response["intents"][i]["confidence"]
                    logger.info("There is " + new_intent + " with confidence " + str(new_confidence_rate))
                    if confidence_rate < new_confidence_rate:
                        intent = new_intent
                        confidence_rate = new_confidence_rate
            logger.info("Intent: " + intent)
            return intent.replace("_", " ")
        else:
            logger.info("No intent detected.")
            return False
        
    def extract_entity(self, response):
        logger = logging.getLogger(__name__)
        
        logger.info("Entity extraction")
        #If entities are detected, we take the one with the best confidence
        if response["entities"]:
            entity = response["entities"][0]["value"]
            entity_type = response["entities"][0]["entity"]
            confidence_rate = response["entities"][0]["confidence"]
            logger.info("There is value " + entity + " of entity " + entity_type + " with confidence " + str(confidence_rate))
    
            if len(response["entities"]) > 1:
                for i in range(1, len(response["entities"])):
                    new_entity = response["entities"][i]["value"]
                    new_entity_type = response["entities"][i]["entity"]
                    new_confidence_rate = response["entities"][i]["confidence"]
                    logger.info("There is " + new_entity + " of type " + new_entity_type + " with confidence " + str(new_confidence_rate))
            
                    if confidence_rate < response["entities"][i]["confidence"]:
                        entity = new_entity
                        entity_type = new_entity_type
                        confidence_rate = new_confidence_rate
    
            logger.info("Entity: " + entity)
            return entity, entity_type
        else:
            logger.info("No entity detected.")
            return False, False
        
    def configure_with_dataset(self, df):
        logger = logging.getLogger(__name__)
        
        self.upload_list_intents()
        self.upload_list_entities()
        
        logger.info("Configuration of the assistant depending on the dataset.")
        
        self.print_intents()
        
        logger.info("We create the intents with the name of the columns (if the intent already exists, we do nothing)")
        for column in df.columns:
            logger.info("Column: " + column)
            self.create_intent_to_workspace(column)
        
        self.print_intents_and_examples()
        
        # we list the entities
        self.print_entities()
    
        # we create the missing entities
        logger.info("We create the entities with the name of the columns and the values their contents (if already existed, nothing is done)")
        for column in df.columns:
            logger.info("Column: " + column)
            self.create_entity_to_workspace(column, df[column])
    
        # we print the entities and their examples
        self.print_entities_and_values()
        
    def configure_with_database(self, database):
        logger = logging.getLogger(__name__)
        
        self.upload_list_intents()
        self.upload_list_entities()
        
        logger.info("Configuration of the assistant depending on the JSON database.")
        
        self.print_intents()
        
        logger.info("We create the intents (if the intent already exists, we do nothing)")
        for intent in database.get_list_sub_key():
            logger.info("Intent: " + intent)
            self.create_intent_to_workspace(intent)
        
        self.print_intents_and_examples()
        
        # we list the entities
        self.print_entities()
        
        # we create the missing entities
        logger.info("We create the entities (if already existed, nothing is done)")
        for entity in database.get_list_sub_key_with_attributes():
            logger.info("Entity: " + entity)
            self.create_entity_to_workspace(entity, database.get_list_sub_key_values()[entity])
    
        # we print the entities and their examples
        self.print_entities_and_values()
        
        # we configure the dialog tree
        self.configure_dialog_tree(database)
        
    def configure_dialog_tree(self, database):
        logger = logging.getLogger(__name__)
        
        logger.info("We are configuring the dialog tree.")
        