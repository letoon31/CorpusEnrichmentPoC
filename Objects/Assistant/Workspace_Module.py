import logging

class Workspace_Module():
    
    ###############################
    # GET THE LIST OF WORKSPACE ###
    ###############################
    def get_workspace_list(self, nodejsconnector):
        response = nodejsconnector.list_workspaces()
        
        workspaces = []
        
        for workspace in response["workspaces"]:
            workspaces.append([workspace["name"], workspace["workspace_id"]])
        
        return workspaces
    
    def create_new_workspace(self, nodejsconnector, workspace_name, workspace_description = 'A new workspace'):
        logger = logging.getLogger(__name__)
        
        logger.info("Now we are creating our new workspace (if it is already created, nothing is done)")

        # we get the list of workspaces, we identify our workspace by its name
        workspaces_list = self.get_workspace_list(nodejsconnector)

        already_exist = False
        for workspace in workspaces_list:
            logger.info("Already existed workspace: " + workspace[0])
            if workspace[0] == workspace_name:
                already_exist = True
        
        if already_exist:
            logger.info("The workspace already exists, nothing is done")
        else:
            logger.info("Our workspace " + workspace_name + " doesn't exist, so we are creatint a workspace with this name.")
            nodejsconnector.create_workspace(workspace_name, workspace_description)
    
    # remove a workspace
    def remove_workspace(self, nodejsconnector, workspace_id = ""):
        logger = logging.getLogger(__name__)
        logger.info("Removing the workspace")
        nodejsconnector.remove_workspace(workspace_id)
                
    # function returning the id of the workspace
    def retrieve_workspace_id(self, nodejsconnector, workspace_name):
        logger = logging.getLogger(__name__)
        
        logger.info("Searching the ID of the workspace " + workspace_name)
        logger.info("We list the workspaces and their ID.")
        workspace_id = ""

        workspace_list = self.get_workspace_list(nodejsconnector)
        for workspace in workspace_list:
            logger.info("\nName: " + workspace[0] + "\n" + "Id: " + workspace[1])
    
            if workspace[0] == workspace_name:
                workspace_id = workspace[1]
    
        logger.info("The Id of our workspace is " + workspace_id)
        
        return workspace_id
    
    def remove_all_workspaces(self, nodejsconnector):
        workspaces = self.get_workspace_list(nodejsconnector)
        
        for workspace in workspaces:
            self.remove_workspace(nodejsconnector, workspace[1])