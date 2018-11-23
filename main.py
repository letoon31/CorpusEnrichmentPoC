"""
Automatic Corpus/ Dataset Enrichment
Code by Elie Azeraf, IBM
"""

import os
import logging
os.chdir(os.path.dirname(os.path.realpath("main.py")))

# we do all the needed importations
from Objects.Gandalf import Gandalf
from Objects.Assistant.Assistant import Assistant
from Objects.MyJSONDatabase import MyJSONDatabase
from Objects.EntityTypeClf import EntityTypeClf
from Objects.Orchestra import Orchestra
from Objects.IntentEntityExtractor import IntentEntityExtractor

#################################
### CREATION OF THE ORCHESTRA ###
#################################

orchestra = Orchestra()

# logger initialisation
orchestra.configure_logger()
logger = logging.getLogger(__name__)
orchestra.presentation()


###############################
### CREATION OF THE DATASET ###
###############################

database = MyJSONDatabase()
database.print_database()

#################################
### INITIALISATION OF GANDALF ###
#################################

gandalf = Gandalf()
logger.info('Gandalf is initialised.')


###############################################
### CREATION/CONFIGURATION OF THE ASSISTANT ###
###############################################

assistant = Assistant(remove_workspaces = True)
logger.info("The assistant is created.")
assistant.configure_with_database(database)

###############################################
### CREATION OF THE INTENT/ENTITY EXTRACTOR ###
###############################################

intent_entity_extractor = IntentEntityExtractor()
logger.info("The intent/entity extractor is created.")


##############################################
### CREATION OF THE ENTITY TYPE CLASSIFIER ###
##############################################

entity_clf = EntityTypeClf()
logger.info("The entity clf is created.")


#####################################
## CONFIGURATION OF THE ORCHESTRA ###
#####################################

orchestra.configure_params(assistant, database, intent_entity_extractor, gandalf, entity_clf)


###################
## Questionning ###
###################

orchestra.interactive_mode()