import json
import logging

class MyJSONDatabase():
    
    def __init__(self, path_data = "data/example_data/superheroes_basic.json"):
        with open(path_data) as f:
            self.data = json.load(f)
            
        for sub_key in self.get_list_sub_key():
            for key in self.data.keys():
                good_key = True
                
                if sub_key not in self.data[key]:
                    good_key = False
                elif key != self.data[key][sub_key]:
                    good_key = False
            
            if good_key:
                self.main_sub_key = sub_key
            
    def print_database(self):
        string_json = json.dumps(self.data, indent = 4)
        print(string_json)
        
    def add_key(self, key):
        self.data[key] = {}
        
    def add_element(self, infos):
        for info in infos:
            self.data[info["Key"]][info["Entity"]] = info["Value"]
            
    def get_list_sub_key(self):
        set_sub_key = set()
        
        for key in self.data.keys():
            for sub_key in self.data[key].keys():
                set_sub_key.update([sub_key])
                
        return set_sub_key
    
    def get_list_sub_key_with_attributes(self):
        set_sub_key = set()
        
        for key in self.data.keys():
            for sub_key in self.data[key].keys():
                set_sub_key.update([sub_key])
                
        set_sub_key.update(["Attributes"])
                
        return set_sub_key
    
    def get_list_sub_key_values(self):
        dict_sub_key = dict.fromkeys(self.get_list_sub_key())
        for key in dict_sub_key:
            dict_sub_key[key] = []
        dict_sub_key["Attributes"] = []
        
        
        for key in self.data.keys():
            for sub_key in self.data[key].keys():
                if type(self.data[key][sub_key]) == dict:
                    sub_dict = self.data[key][sub_key]
                    for key, value in sub_dict.items():
                        dict_sub_key[sub_key].append(value)
                        dict_sub_key["Attributes"].append(key)
                else:
                    dict_sub_key[sub_key].append(self.data[key][sub_key])
                
        return dict_sub_key
    
    def checking_if_answer_in_database(self, intent, entity, entity_value):
        for key in self.data.keys():
            if entity in self.data[key]:
                if self.data[key][entity] == entity_value:
                    if intent in self.data[key]:
                        return True, self.data[key][intent]
            
        return False, None
    
    def add_information(self, intent, entity, entity_value, answer):
        logger = logging.getLogger(__name__)
        
        for key in self.data.keys():
            if entity in self.data[key]:
                if self.data[key][entity] == entity_value:
                    self.data[key][intent] = answer
                    logger.info("The information '" + answer + "' is added in our database.")
                    
                    return
                
        if entity == self.main_sub_key:
            self.add_key(entity_value)
            
            self.data[entity_value][entity] = entity_value
            self.data[entity_value][intent] = answer
        
        logger.info("Impossible to add this information")
        
        