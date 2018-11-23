from Naked.toolshed.shell import muterun_js
import json
import os

class NodeJSConnector():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.path_functions = (os.path.dirname(__file__) + "/NodeJSFunctions/").replace("\\", "/")
        
    def set_workspace_id(self, workspace_id):
        self.workspace_id = workspace_id
        
    def list_workspaces(self):
        response = muterun_js(self.path_functions + 'call_list_workspace.js ' + self.username + ' ' + self.password)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def list_intents(self):
        response = muterun_js(self.path_functions + 'call_list_intents.js ' + self.username + ' ' + self.password + ' ' + self.workspace_id)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def create_workspace(self, name, description):
        name = name.replace(" ", "_")
        description = description.replace(" ", "_")
        response = muterun_js(self.path_functions + 'call_create_workspace.js ' + self.username + ' ' + self.password + ' ' + name + ' ' + description)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def list_entities(self):
        response = muterun_js(self.path_functions + 'call_list_entities.js ' + self.username + ' ' + self.password + ' ' + self.workspace_id)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def create_intent(self, intent):
        intent = intent.replace(" ", "_")
        response = muterun_js(self.path_functions + 'call_create_intent.js ' + self.username + ' ' + self.password + ' ' + self.workspace_id + ' ' + intent)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
        
    def create_entity(self, entity):
        entity = entity.replace(" ", "_")
        response = muterun_js(self.path_functions + 'call_create_entity.js ' + self.username + ' ' + self.password + ' ' + self.workspace_id + ' ' + entity)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def list_examples(self, intent):
        intent = intent.replace(" ", "_")
        response = muterun_js(self.path_functions + 'call_list_examples.js ' + self.username + ' ' + self.password + ' ' + self.workspace_id + ' ' + intent)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def list_values(self, entity):
        entity = entity.replace(" ", "_")
        response = muterun_js(self.path_functions + 'call_list_values.js ' + self.username + ' ' + self.password + ' ' + self.workspace_id + ' ' + entity)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def create_value(self, entity, value):
        entity = entity.replace(" ", "_")
        value = value.replace(" ", "_")
        response = muterun_js(self.path_functions + 'call_create_value.js ' + self.username + ' ' + self.password + ' ' + self.workspace_id + ' ' + entity + ' ' + value)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def message(self, message):
        message = message.replace(" ", "_")
        response = muterun_js(self.path_functions + 'call_message.js ' + self.username + ' ' + self.password + ' ' + self.workspace_id + ' ' + message)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
    
    def remove_workspace(self, workspace_id = ""):
        if workspace_id == "":
            workspace_id = self.workspace_id
            
        response = muterun_js(self.path_functions + 'call_delete_workspace.js ' + self.username + ' ' + self.password + ' ' + workspace_id)
        my_json = response.stdout.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        
        return data
        
    