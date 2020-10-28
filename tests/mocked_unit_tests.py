import unittest
import unittest.mock as mock
from dotenv import load_dotenv
import os
import datetime
from freezegun import freeze_time
from os.path import join, dirname
import requests
import bot
from bot import KEY_BOT_COMMAND, KEY_MESSAGE
import app
import models

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_EMIT = "emit"
KEY_CHANNEL = "channel"
KEY_ID = 0
freezer = freeze_time("2020-10-27 21:24:00")
freezer.start()


dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)


database_uri = os.environ['DATABASE_URL']



botty = bot.Bot()
db = app.db
mess = models.Messages("hi there", 1)
user = models.user_info("bot@gmail.com", "bot", "pic")

class MockedDateResponse:
    def __init__(self, date):
        self.date = date
        
class MockedJokeResponse:
    def __init__(self, joke):
        self.joke = joke

class MockedTranslateResponse:
    def __init__(self, text):
        self.text = text

class MockedDBAddResponse:
    def __init__(self, message, message_id):
        self.message = message
        self.message_id = message_id

class MockedUserEmitResponse:
    def __init__(self, all_users):
        self.all_users = all_users
        
class MockedCountEmitResponse:
    def __init__(self, user_count):
        self.user_count = user_count
        
class MockedMessagesEmitResponse:
    def __init__(self, all_messages):
        self.all_messages = all_messages

class logicTestCase(unittest.TestCase):
    def setUp(self):
        self.date_success_test_params = [
            {
                KEY_INPUT: "!! date",
                KEY_EXPECTED: "2020-10-27 21:24:00"
            }
        ]
        self.models_messages_success_test_params = [
            {
                KEY_INPUT: mess.message,
                KEY_EXPECTED: "hi there"
            }
        ]
        self.app_emit_count_success_test_params = [
            {
                KEY_INPUT: 'emit_user_count',
                KEY_EXPECTED: 0
            }
        ]
        self.app_emit_users_success_test_params = [
            {
                KEY_INPUT: 'emit_all_users',
                KEY_CHANNEL: "channel",
                KEY_EXPECTED: []
            }
        ]
        self.app_emit_messages_success_test_params = [
            {
                KEY_INPUT: 'emit_all_messages',
                KEY_CHANNEL: "channel",
                KEY_EXPECTED: []
            }
        ]

    def mocked_api_search(self, q):
        return [
            MockedDateResponse(
                "2020-10-27 21:24:00"),
            MockedUserEmitResponse(
                { KEY_CHANNEL: {"all_users": app.all_users}}),
            MockedCountEmitResponse(
                { KEY_CHANNEL: {"user_count": app.user_count}}),
            MockedMessagesEmitResponse( 
                { KEY_CHANNEL: {"all_messages": app.all_messages}})
            ]

    def test_bot_date_success(self):
        for test_case in self.date_success_test_params:
            with mock.patch('datetime.date'):
                response = str(datetime.datetime.today())
                freezer.stop()
                print(response)

            expected = test_case[KEY_EXPECTED]
            print(expected)

            self.assertEqual(response, expected)


    def test_models_messages_success(self):
        for test_case in self.models_messages_success_test_params:
            with mock.patch('models.Messages.__repr__', self.mocked_api_search):
                response = mess.message
                print(response)
            expected = test_case[KEY_EXPECTED]
            print(expected)
            
            self.assertEqual(response, expected)

    def test_app_emit_count_success(self):
        for test_case in self.app_emit_count_success_test_params:
            with mock.patch('app.emit_user_count'):
                response = app.user_count
                print(response)
            expected = test_case[KEY_EXPECTED]
            print(expected)
            
            self.assertEqual(response, expected)

    def test_emit_users_success(self):
        for test_case in self.app_emit_users_success_test_params:
            with mock.patch('app.emit_all_users', self.mocked_api_search):
                response = app.all_users
                print(response)
            expected = test_case[KEY_EXPECTED]
            print(expected)
            
            self.assertEqual(response, expected)

    def test_emit_messages_success(self):
        for test_case in self.app_emit_messages_success_test_params:
            with mock.patch('app.emit_all_messages', self.mocked_api_search):
                response = app.all_messages
                print(response)
            expected = test_case[KEY_EXPECTED]
            print(expected)
            
            self.assertEqual(test_case[KEY_EXPECTED], expected)

if __name__ == '__main__':
    unittest.main()
