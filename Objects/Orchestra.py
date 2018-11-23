import logging
from Objects.Graphics.MainWindow import MainWindow

class Orchestra():
    
    def __init__(self):
        return
    
    def configure_params(self, assistant = None, database = None, intent_entity_extractor = None, gandalf = None, entity_clf = None):
        self.assistant = assistant
        self.database = database
        self.intent_entity_extractor = intent_entity_extractor
        self.gandalf = gandalf
        self.entity_clf = entity_clf
    
    def presentation(self, title = "DATASET ENRICHMENT/COMPLETION PROJECT"):
        number_dash = len(title)
        
        dash_line = "-" * (number_dash + 3*2 + 2)
        title_line = "-" * 3 + " " + title.upper() + " " + "-" * 3
        signature = "IBM Project by Elie Azeraf"
        signature_line = " " * (len(dash_line) - len(signature)) + signature + "\n\n"
                                
        print(dash_line)
        print(dash_line)
        print(title_line)
        print(dash_line)
        print(dash_line)
        print(signature_line)

    def configure_logger(self):
        want_logger = input("Do you want to see the logs ? (y/n): ")
        
        if want_logger == "n":
            return 
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s: [%(message)s]', '%I:%M:%S %p')
        console = logging.StreamHandler()
        console.setFormatter(fmt)
        logger.addHandler(console)
    
        #return logger
    
    def construt_question(self, entity, intent):
        return "What is the " + intent.lower() + " of " + entity + " ?"
            
    def interactive_mode(self):
        interactive = True
        
        while(interactive):
            print("What do you want to do ? (type the number)")
            print("1 - Ask a question")
            print("2 - Show me the dataset")
            print("3 - Show me my intents and entities !")
            print("4 - Quit")
            
            choice = input("Your choice please: ")
            
            print("Cool")
            if choice == "1":
                print("Choice 1")
                question = input("Your question: ")
                self.ask_simple_question(question)
            elif choice == "2":
                print("Choice 2")
                self.database.print_database()
            elif choice == "3":
                print("Choice 3")
                self.assistant.print_intents_and_examples()
                self.assistant.show_entities_and_values()
            elif choice == "4":
                print("Choice 4")
                interactive = False
                self.assistant.remove_workspace()
        
    def ask_simple_question(self, question):
        print("The question is:", question)
        logger = logging.getLogger(__name__)
    
        response = self.assistant.send_question(question)
        intent = self.assistant.extract_intent(response)
        entity_value, entity = self.assistant.extract_entity(response)
        
        logger.info("\n\nINTENT/ENTITY IDENTIFICATION\n")
        
        logger.info("Intent: " + str(intent))
        logger.info("Entity: " + str(entity) + ", value: " + str(entity_value))
        
        answer_in_database, answer = self.database.checking_if_answer_in_database(intent, entity, entity_value)
        
        if answer_in_database:
            logger.info("The answer is in our database.")
            print("The answer is:", answer)

            return
        
        logger.info("The answer is not in our database")
        
        if not intent and entity_value:
            logger.info("We don't have the intent, and we have the entity.")
            logger.info("We have to extract the intent.")
            
            intent = self.intent_entity_extractor.extract_intent(question)
            logger.info("Extracted intent: " + intent)
            
            new_intent_added = True
            new_entity_added = False
        
        elif not entity_value and intent:
            logger.info("We don't have the entity, and we have the intent.")
            logger.info("We have to extract the entity.")
            
            entity_value = self.intent_entity_extractor.extract_entity_value(question, intent)
            logger.info("Extracted entity value: " + entity_value)
            
            logger.info("The CLF finds the entity.")
            self.entity_clf.train(self.database.get_list_sub_key_values())
            entity = self.entity_clf.predict_entity_type(entity_value)
            logger.info("Entity: " + entity)
            
            new_intent_added = False
            new_entity_added = True
            
        elif not intent and not entity_value:
            logger.info("We don't have the entity and the intent")
            logger.info("We have to extract both.")
            
            intent, entity_value = self.intent_entity_extractor.extract_all(question)
            logger.info("Extracted intent: " + intent)
            logger.info("Extracted entity value: " + entity_value)
            
            logger.info("The CLF finds the entity.")
            self.entity_clf.train(self.database.get_list_sub_key_values())
            entity = self.entity_clf.predict_entity_type(entity_value)
            logger.info("Entity: " + entity)
            
            new_intent_added = True
            new_entity_added = True
            
        else:
            new_intent_added = False
            new_entity_added = False
            
        logger.info("\n\nASKING THE QUESTION TO GANDALF AND DATABASE ENRICHMENT\n")    
        
        logger.info("We ask the question to Gandalf: " + question)
        gandalf_answer = self.gandalf.answer_question(question)
        logger.info("Answer of Gandalf: '" + gandalf_answer + "'")
        print("The answer is: " + gandalf_answer)
        
        self.database.add_information(intent, entity, entity_value, gandalf_answer)
        
        self.automatic_enrichment(question, new_intent_added, new_entity_added, intent, entity, entity_value)
        
        logger.info("\n\nADDING THE INFORMATION TO THE ASSISTANT\n")
        self.assistant.configure_with_database(self.database)
        
    
    def automatic_enrichment(self, question, new_intent_added, new_entity_added, intent, entity, entity_value):
        logger = logging.getLogger(__name__)
        
        dict_data = self.database.get_list_sub_key_values()
        
        if new_intent_added:
            for value in dict_data[entity]:
                answer_in_database, answer = self.database.checking_if_answer_in_database(intent, entity, value)
                if not answer:
                    new_question = question.replace(entity_value, value)
                    logger.info("We ask the question to Gandalf: " + new_question)
                    gandalf_new_answer = self.gandalf.answer_question(new_question)
                    logger.info("Answer of Gandalf: '" + gandalf_new_answer + "'")
                    
                    self.database.add_information(intent, entity, value, gandalf_new_answer)
                    
        if new_entity_added:
            for new_entity in self.database.get_list_sub_key():
                answer_in_database, answer = self.database.checking_if_answer_in_database(new_entity, entity, entity_value)
            
                if not answer_in_database:
                    logger.info(entity_value + " doesn't have the information " + new_entity)
                
                    new_question = self.construt_question(entity_value, new_entity)
                    logger.info("We ask the question to Gandalf: " + new_question)
                    gandalf_new_answer = self.gandalf.answer_question(new_question)
                    logger.info("Answer of Gandalf: '" + gandalf_new_answer + "'")
                
                    self.database.add_information(new_entity, entity, entity_value, gandalf_new_answer)
        
        
    def interactive_mode_continuing(self):
        interactive = True
        
        while(interactive):
            print("What do you want to do ? (type the number)")
            print("1 - Continue the demo !")
            print("2 - Show me the dataset")
            print("3 - Show me my intents and entities !")
            
            choice = input("Your choice please: ")
            
            if choice == "1":
                interactive = False
            elif choice == "2":
                self.database.print_database()
            elif choice == "3":
                self.assistant.show_intents_and_examples()
                self.assistant.show_entities_and_values()
            
            print("\n")
            
    def interactive_mode_only_questionning(self):
        interactive = True
        
        while(interactive):
            print("What do you want to do ? (type the number)")
            print("1 - Ask a question")
            print("2 - Quit")
            
            choice = input("Your choice please: ")
            
            if choice == "1":
                question = input("Your question: ")
                answer = self.gandalf.answer_question(question)
                print("\nAnswer:", answer, "\n")
            elif choice == "2":
                interactive = False
    
    def interactive_mode_window(self):
        main_window = MainWindow("The Batman Project")
        
        main_window.mainloop()
        
        interactive = True
        
        while(interactive):
            print("What do you want to do ? (type the number)")
            print("1 - Ask a question")
            print("2 - Show me the dataset")
            print("3 - Show me my intents and entities !")
            print("4 - Quit")
            
            choice = input("Your choice please: ")
            
            if choice == "1":
                question = input("Your question: ")
                self.ask_simple_question(question)
            elif choice == "2":
                self.database.print_database()
            elif choice == "3":
                self.assistant.show_intents_and_examples()
                self.assistant.show_entities_and_values()
            elif choice == "4":
                interactive = False
                self.assistant.remove_workspace()