import unittest # Importing the unittest module
from user import User # Importing the User

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User('mukhtarabdirahman') # created user object 
    
if __name__ == '__main__':
    unittest.main()