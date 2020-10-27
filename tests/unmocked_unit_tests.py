import unittest
import unittest.mock as mock
from dotenv import load_dotenv
import os
import datetime
from os.path import join, dirname
import app
import bot
from bot import KEY_BOT_COMMAND, KEY_MESSAGE
import models

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_LENGTH = "length"
KEY_FIRST_WORD = "first_word"
KEY_SECOND_WORD = "second_word"
botty = bot.Bot()


class parsingLogicTestCase(unittest.TestCase):
    def setUp(self):
        self.bot_about_success_test_params = [
            {
                KEY_INPUT: "!! about",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "I am Awesome Bot! I can translate any sentence you want into leetspeak! I can also tell you a random joke and today's date! Aren't I awesome?"
                    }
            }
        ]
        self.bot_help_success_test_params = [
            {
                KEY_INPUT: "!! help",
                KEY_EXPECTED: {
                    KEY_MESSAGE: 'These are the commands I currently understand: about, help, funtranslate <message>, date, joke.    -REMEMBER- each command but begin with "!! " or else I wont understand you! ex: "!! joke"'
                    }
            },
        ]

    def test_about_success(self):
        for test in self.bot_about_success_test_params:
            response = bot.switch(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response[KEY_MESSAGE], expected[KEY_MESSAGE])
            # Alternatively (and preferably), you can do self.assertDictEqual(response, expected)

    def test_help_success(self):
        for test in self.bot_help_success_test_params:
            response = bot.switch(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response, expected)
            # Alternatively (and preferably), you can do self.assertDictEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
