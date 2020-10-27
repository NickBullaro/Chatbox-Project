import unittest
import unittest.mock as mock
from dotenv import load_dotenv
import os
from datetime import date
from os.path import join, dirname
import requests
import bot
import app
import models

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

class logicTestCase(unittest.TestCase):
    def setUp(self):
        self.joke_success_test_params = [
            {
                KEY_INPUT: "!! joke",
                KEY_EXPECTED: "terrible joke"
            }
        ]
        self.date_success_test_params = [
            {
                KEY_INPUT: "!! date",
                KEY_EXPECTED: "10/15/2020, 21:24"
            }
        ]
        self.translate_success_test_params = [
            {
                KEY_INPUT: "!! funtranslate hello",
                KEY_EXPECTED: "h3lL0"
            },
        ]
    
    def mocked_bot_api_calls(self, q, count):
        return [
            MockedDateResponse(
                "mocked date"),
            MockedJokeResponse(
                "mocked joke"),
            MockedTranslateResponse(
                "mocked translate")
            ]

    def test_bot_joke_success(self):
        for test_case in self.joke_success_test_params:
            with mock.patch('requests.request', self.mocked_bot_api_calls):
                print("hi")
            expected = test_case[KEY_EXPECTED]
            print(expected)
            
            self.assertEqual(test_case[KEY_EXPECTED], expected)

    def test_bot_date_success(self):
        for test_case in self.date_success_test_params:
            with mock.patch('datetime.date') as mock_date:
                mock_date.today.return_value = date(2020, 10, 27)
                mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
                
                print("yo")
            expected = test_case[KEY_EXPECTED]
            print(expected)

            self.assertEqual(test_case[KEY_EXPECTED], expected)

    def test_bot_translate_success(self):
        for test_case in self.translate_success_test_params:
            with mock.patch('requests.get', self.mocked_bot_api_calls):
                print("sup")
            expected = test_case[KEY_EXPECTED]
            print(expected)
            
            self.assertEqual(test_case[KEY_EXPECTED], expected)
        
if __name__ == '__main__':
    unittest.main()
