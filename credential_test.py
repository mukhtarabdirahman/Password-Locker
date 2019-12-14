import unittest # Importing the unittest module
from credential import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential ('mukhtarabdirahman', 'codePanther') # created credential object
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.username,'mukhtarabdirahman') 
        self.assertEqual(self.new_credential.password,'codePanther') 
    def test_save_credential(self):
        """
        test_save_credential test case to test if the contact object is saved into
        the credential list
        """
        self.new_credential.save_credential()# saving the new credential
if __name__ == '__main__':
    unittest.main()
        
