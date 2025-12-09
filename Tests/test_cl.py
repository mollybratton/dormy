import unittest
from ProductionCode.helper_functions import *
import subprocess
from ProductionCode.datasource import *

data = DataSource()

class Test_Functions(unittest.TestCase):

    def test_get_ses_by_county(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs a test to see if the function get_ses_by_county() is functioning correctly'''
        result = data.getSESByCounty("Anoka")
        self.assertIn("('Anoka', 1.0660279, 3)", str(result))

    def test_get_scores_by_county(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs a test to see if the function get_scores_by_county() is functioning correctly'''
        result = data.getScoresByCounty("Anoka")
        self.assertIn("('Anoka', 0.4537864812, 3)", str(result))

    def test_county_name_ses_invalid(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs a test to see if the function get_ses_by_county() returns a message if an invalid county name is entered'''
        result = data.getSESByCounty("invalid")
        self.assertEqual(result, [])
    
    def test_invalid_county_name_scores(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs a test to see if the function get_scores_by_county() returns a message if an invalid county name is entered'''
        result = data.getScoresByCounty("Nothing")
        self.assertEqual(result, [])


    def test_main_ses(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs a test to see if the main function is functioning correctly'''
        code = subprocess.Popen(['python3', 'command_line.py', '--ses', 'Carlton'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "[('Carlton', 0.5387626, 3), ('Carlton', 0.5387626, 3), ('Carlton', 0.5387626, 4), ('Carlton', 0.5387626, 4), ('Carlton', 0.5387626, 5), ('Carlton', 0.5387626, 5), ('Carlton', 0.5387626, 6), ('Carlton', 0.5387626, 6), ('Carlton', 0.5387626, 7), ('Carlton', 0.5387626, 7), ('Carlton', 0.5387626, 8), ('Carlton', 0.5387626, 8)]")

    def test_main_scores(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs a test to see if the main function is functioning correctly'''
        code = subprocess.Popen(['python3', 'command_line.py', '--scores', 'Carlton'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "[('Carlton', 0.6371980389, 3), ('Carlton', 0.4407366963, 3), ('Carlton', 0.3835034064, 4), ('Carlton', 0.1317242609, 4), ('Carlton', 0.5604280513, 5), ('Carlton', 0.2172994698, 5), ('Carlton', 0.4299263383, 6), ('Carlton', 0.2390210295, 6), ('Carlton', 0.152215916, 7), ('Carlton', 0.0982295122, 7), ('Carlton', 0.076772927, 8), ('Carlton', 0.0340384543, 8)]")

    def test_main_ses_number(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs an edge test to see if the main function returns no mathcing county if input entered incorrectly'''
        code = subprocess.Popen(['python3', 'command_line.py', '--ses', '20'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "[]")

    def test_main_scores_number(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs an edge test to see if the main function returns no mtaching county if input entered incorrectly'''
        code = subprocess.Popen(['python3', 'command_line.py', '--scores', '100'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "[]")

    def test_main_scores_no_input(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs an edge test to see if the main function returns no mtaching county if no input entered'''
        code = subprocess.Popen(['python3', 'command_line.py', '--scores', ''],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "Usage statement: python3 command_line.py --ses 'countyname' or python3 command_line.py --scores 'countyname'")


    def test_main_ses_no_input(self):
        '''Arguments: self
        Return value: None
        Purpose: Runs an edge test to see if the main function returns usage statement if no input entered'''
        code = subprocess.Popen(['python3', 'command_line.py', '--ses', ''],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "Usage statement: python3 command_line.py --ses 'countyname' or python3 command_line.py --scores 'countyname'")

