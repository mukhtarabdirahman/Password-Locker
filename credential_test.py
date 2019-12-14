import unittest # Importing the unittest module
from credential import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential ('mukhtarabdirahman', 'codePanther') # created credential object
        
