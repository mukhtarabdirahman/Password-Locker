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
        # self.new_credential.save_credential()
        # self.assertEqual(len(Credential.credential_list),1)
   
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credential.credential_list = []
    def test_save_multiple_credential(self):
        """
        test_save_multiple_credential to check if we can save multiple credntial
        objects to our credential_listself.assertEqual(len(Credential.credential_list),1)
        """
        
        self.new_credential.save_credential()
        test_credential = Credential('Ahmed','hajia')
        test_credential.save_credential()
        # self.assertEqual(len(Credential.credential_list),2)
        
    def test_delete_credential(self):
        """
        test_delete_credential to test if we can remove a user from our user list
        """
        self.new_credential.save_credential()
        test_credential = Credential('Ahmed','hajia')
        test_credential.save_credential()
        
        # self.new_credential.delete_credential()
        # self.assertEqual(len(Credential.credential_list),1)
    def test_find_credential_by_username(self):
        """
        Test to find out if we can find credential by username and display information
        """
        self.new_credential.save_credential()
        test_credential = Credential('Ahmed','hajia')
        test_credential.save_credential()
        
        found_credential = Credential.find_by_username('Ahmed')
        # self.assertEqual(found_credential.password, test_credential.password)
        
    def test_if_credential_exists(self):
        """
        Test to see if a given credential exists
        """
        self.new_credential.save_credential()
        test_credential = Credential('Ahmed','hajia')
        test_credential.save_credential()
        
        credential_exists = Credential.credential_exist('Ahmed')
        # self.assertTrue(credential_exists)
    def test_display_all_credential(self):
        """
        Method that returns a list of all credential saved
        """
        # self.assertEqual(Credential.display_all_credentials(),Credential.credential_list)
        
        
        
        
        
        
        
        
   
    
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
        
