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
        save_user method saves credential objects into credential_list
        # """
        # Credential.credential_list.append(self)
    def delete_credential(self):
        """
        delete_credential method deletes a saved user from the credential_list
        """
        # Credential.credential_list.remove(self)
        
    @classmethod
    def find_by_username(cls,username):
        """
        check if credential exist
        """
        for credential in cls.credential_list:
            if credential.username == username:
                 return credential
    @classmethod
    def credential_exist(cls,username):
        """
        check if a credential exist
        """
        for credential in cls.credential_list:
            if credential.username == username:
                 return credential
             
    @classmethod
    def display_all_credentials(cls):
        """
        method that returns the credential list
        """
        return cls.credentials_list
            
        
       
        
        
        
   
   
    
    