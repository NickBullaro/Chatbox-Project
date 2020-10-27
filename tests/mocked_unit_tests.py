import unittest
import unittest.mock as mock
from dotenv import load_dotenv
import os
import datetime
from os.path import join, dirname
import requests
import bot

KEY_INPUT = "input"
KEY_EXPECTED = "expected"


dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)


database_uri = os.environ['DATABASE_URL']





class MockedDateResponse:
    def __init__(self, date):
        self.date = date
        
class MockedJokeResponse:
    def __init__(self, joke):
        self.joke = joke

class MockedTranslateResponse:
    def __init__(self, text):
        self.text = text

class TwitterQueryTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!date",
                KEY_EXPECTED: "10/15/2020, 21:24"
            },
            {
                KEY_INPUT: "!!joke",
                KEY_EXPECTED: "terrible joke"
            },
            {
                KEY_INPUT: "!!funtranslate hello",
                KEY_EXPECTED: "Two dyslexics walk into a bra."
            },
        ]
        
    def mocked_random_choice(self, values):
        return values[0]
    
    def mocked_bot_api_calls(self, q, count):
        return [
            MockedDateResponse(
                "mocked date"),
            MockedJokeResponse(
                "mocked joke"),
            MockedTranslateResponse(
                "mocked translate")
            ]

    def test_bot_calls_success(self):
        for test_case in self.success_test_params:
            with mock.patch('requests.request', self.mocked_bot_api_calls):
                print("hi")

            expected = test_case[KEY_EXPECTED]
            print(expected)
            
            self.assertEqual(test_case[KEY_EXPECTED], expected)
        
if __name__ == '__main__':
    unittest.main()
