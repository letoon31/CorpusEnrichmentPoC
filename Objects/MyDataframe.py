import pandas as pd
import logging

class MyDataframe(pd.DataFrame):
    
    def __init__(self):
        list_name = ["Batman", "Superman"]
        list_city = ["Gotham", "Metropolis"]
    
        columns = ["Name", "City"]
        
        super().__init__(columns = columns)
        self["Name"] = list_name
        self["City"] = list_city
        
    def print_dataset(self):
        print("Your dataset:")
        with pd.option_context('display.max_rows', None, 'display.max_columns', len(self.columns)):
            print(self)
        print("")
        
    def big_superhero_dataset(self):
        columns = ["Name", "City"]
        pd.DataFrame.__init__(self, columns = columns)
        
        list_name = ["Batman", "Superman", "Iron Man", "Hulk", "Wonder Woman", "Nightwing", "Thor"]
        list_city = ["Gotham", "Metropolis", "New York", "New York", "No Entry", "Chicago", "New York"]
        list_secret_identity = ["Bruce Wayne", "Clark Kent", "Tony Stark", "Bruce Banner", "Diana Prince", "Dick Grayson", "Donald Blake"]
        list_archenemy = ["Joker", "Lex Luthor", "The Mandarin", "Abomination", "Ares", "Deathstroke", "Loki"]
        
        self["Name"] = list_name
        self["City"] = list_city
        self["Secret Identity"] = list_secret_identity
        self["Archenemy"] = list_archenemy
        
    def superhero_dataset_version_2(self):
        columns = ["Name", "City", "Secret Identity", "Archenemy", "Actor"]
        pd.DataFrame.__init__(self, columns = columns)
        
    def checking_elements_in_df(self, intent, entity, entity_type):
        logger = logging.getLogger(__name__)
        
        logger.info("We check if these elements are in our dataframe")
        all_elements_in_df = True

        if intent in self.columns:
            logger.info("The intent is a column of our dataframe.")
        else:
            logger.info("This intent is not in the dataframe.")
            all_elements_in_df = False
    
        if entity in list(self[entity_type]):
            logger.info("The entity value is in the dataframe.")
        else:
            logger.info("The entity value is not in the dataframe")
            all_elements_in_df = False
        
        return all_elements_in_df
    
    def add_line(self, line):
        print(line)
        print(self)
        
        index = max(self.index.values) + 1
        self.loc[index] = ""
        
        for column in self.columns:
            self[column][index] = line[column][0]
        
        
        
        