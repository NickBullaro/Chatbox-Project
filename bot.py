import requests
from datetime import date

BOT_PREFIX = "!!"
KEY_IS_BOT = "is_bot"
KEY_BOT_COMMAND = "bot_command"
KEY_MESSAGE = "message"


class Bot():
    def __init__(self):
        self.message = ''
        self.commands = 'about, help, funtranslate <message>, date, joke'
        self.helpString = ''
        self.ft_message = ''
        self.date = ''
        self.rand_joke = ''
    
    
    
    def about(self):
        self.message = "I am Awesome Bot! I can translate any sentence you want into leetspeak! I can also tell you a random joke and today's date! Aren't I awesome?"
        return self.message
        
    def helper(self):
        helpStr = 'These are the commands I currently understand: ' + self.commands + '.    -REMEMBER- each command but begin with "!! " or else I wont understand you! ex: "!! joke"'
        self.helpString = helpStr
        return self.helpString
        
    def funtranslate(self, text):
        base = "https://api.funtranslations.com/translate/leetspeak.json?text=" + text
        req = requests.get(base)
        respo = req.json()
        self.ft_message = respo['contents']['translated']
        return self.ft_message
        
    def dat(self):
        today = date.today()
        self.date = "Today's date is " + str(today)
        return self.date
        
        
    def joke(self):
        url = "https://joke3.p.rapidapi.com/v1/joke"
        headers = {
            'x-rapidapi-host': "joke3.p.rapidapi.com",
            'x-rapidapi-key': "6bd46d61f2mshd2c80482e12a730p16f242jsn3b38dc8f3fb4",
            }
        
        response = requests.request("GET", url, headers=headers)
        respo = response.json()
        self.rand_joke = respo['content']
        return self.rand_joke
        
        
def switch(arg):
    bot = Bot()
    message_components = arg.split(" ")
    
    if message_components[0] != "!!":
        return
    
    if len(message_components) == 2:
        bot_cmd, rest_of_message = message_components[1], ""
    else:
        bot_cmd, rest_of_message = message_components[1], message_components[2:]
        print(rest_of_message)
    
    if bot_cmd == "funtranslate":
        if len(message_components) < 3:
            return "You forgot to enter what you wanted me to translate ya goof!"
        t = ' '.join(rest_of_message)
        return bot.funtranslate(t)
        
    elif bot_cmd == "help":
        return bot.helper()
    elif bot_cmd == "about":
        return bot.about()
    elif bot_cmd == "date":
        return bot.dat()
    elif bot_cmd == "joke":
        return bot.joke()
    else:
        return "Invalid command! Enter '!! help' to see available commands!"