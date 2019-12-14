class Credential:
    '''
    Class to create  account credentials, generate passwords and save their information
    '''
    credentials_list = []
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def save_credential(self):
        """
        save_user method saves credential objects into user_list
        """
        Credential.credentials_list.append(self)
        
    
    