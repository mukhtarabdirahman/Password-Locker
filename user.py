class User:
    """
    Class that generates new instances user
    """
    
    user_list = []
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def save_user(self):
        
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)
    
    def delete_user(self):
        """
        delete_user method deletes a saved user from the user_list
        """
        User.user_list.remove(self)
        
    @classmethod
    def find_by_username(cls,username):
        """
        Method that takes in a name and returns a user that matches that name.
        """
        
        for user in cls.user_list:
            if user.username == username:
                return user
            
            
    @classmethod
    def display_all_users(cls):
        """
        method that returns the user list
        """
        return cls.user_list
    
   
            
   
           
    
        
        
    
        
    
    