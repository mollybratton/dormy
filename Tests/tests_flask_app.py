import unittest
from flask_app import *

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        '''Arguments: self
            Return value: None
            Purpose: Sets up tests_client'''
        self.app = app.test_client()
        self.app.testing = True

        
    def test_homepage(self):
        '''Arguments: self
            Return value: None
            Purpose: Test the homepage route.'''
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Education Gap in Minnesota', response.data)

    def test_ses_valid_county(self):
        '''Arguments: self
            Return value: None
            Purpose: Test SES retrieval for a valid county.'''
        response = self.app.get('/ses/Aitkin')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The socioeconomic status (SES) of Aitkin is: [('Aitkin', 0.3304611, 3), ('Aitkin', 0.3304611, 3), ('Aitkin', 0.3304611, 4), ('Aitkin', 0.3304611, 4), ('Aitkin', 0.3304611, 5), ('Aitkin', 0.3304611, 5), ('Aitkin', 0.3304611, 6), ('Aitkin', 0.3304611, 6), ('Aitkin', 0.3304611, 7), ('Aitkin', 0.3304611, 7), ('Aitkin', 0.3304611, 8), ('Aitkin', 0.3304611, 8)]", response.data)

    def test_ses_invalid_county(self):
        '''Arguments: self
            Return value: None
            Purpose: Test SES retrieval for a nonexistent county.'''
        response = self.app.get('/ses/FakeCounty')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The socioeconomic status (SES) of FakeCounty is: []", response.data)
    
    def test_ses_invalid_number(self):
        '''Arguments: self
            Return value: None
            Purpose: Test SES retrieval for a number imput.'''
        response = self.app.get('/ses/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The socioeconomic status (SES) of 1 is: []", response.data)
    

    def test_scores_valid_county(self):
        '''Arguments: self
            Return value: None
            Purpose: Test scores retrieval for a valid county.'''
        response = self.app.get('/scores/Aitkin')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The test scores of Aitkin are: [('Aitkin', 0.0234525703, 3), ('Aitkin', -0.1062840035, 3), ('Aitkin', -0.2024412934, 4), ('Aitkin', -0.0019590078, 4), ('Aitkin', -0.0869645901, 5), ('Aitkin', -0.1899113464, 5), ('Aitkin', 0.358828883, 6), ('Aitkin', 0.0082180044, 6), ('Aitkin', 0.2288590569, 7), ('Aitkin', -0.1492809693, 7), ('Aitkin', 0.0482046877, 8), ('Aitkin', -0.3741840494, 8)]", response.data)
    
   
    def test_scores_invalid_county(self):
        '''Arguments: self
            Return value: None
            Purpose: Test scores retrieval for a nonexistent county.'''
        response = self.app.get('/scores/FakeCounty')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The test scores of FakeCounty are: []", response.data)
    
    def test_scores_invalid_number(self):
        '''Arguments: self
            Return value: None
            Purpose: Test scores retrieval for a number.'''
        response = self.app.get('/scores/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The test scores of 1 are: []", response.data)

    def test_404_route(self):
        '''Arguments: self
            Return value: None
            Purpose: Checks if the 404 error is working correctly'''
        response = self.app.get('/404', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Page not found. Add /ses/<countyname> or /scores/<countyname> (Do not put space between county names) to the end of the url with a valid MN county name", response.data)

    def test_debug_route(self):
        '''Arguments: self
            Return value: None
            Purpose: Checks if the 500 error is working correctly'''
        response = self.app.get('/Bug/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bug in the code...time to debug', response.data)


if __name__ == '__main__':
    unittest.main()