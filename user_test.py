import unittest # Importing the unittest module
from user import User # Importing the User

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User('mukhtarabdirahman''codePanther') # created user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual() 
        self.assertEqual() 
    
if __name__ == '__main__':
    unittest.main()