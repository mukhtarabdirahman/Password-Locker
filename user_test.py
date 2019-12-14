import unittest # Importing the unittest module
from user import User # Importing the User

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User('mukhtarabdirahman','codePanther') # created user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'mukhtarabdirahman') 
        self.assertEqual(self.new_user.password,'codePanther') 
    def test_save_user(self):
        '''
        test_save_user test case to test if the contact object is saved into
        the user list
        '''
        self.new_user.save_user()# saving the new user
        self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple user
            objects to our user_list
        """
        self.new_user.save_user()
        test_user = User('Ahmed','hajia')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    
    
if __name__ == '__main__':
    unittest.main()