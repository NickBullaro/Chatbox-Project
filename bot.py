import requests
from datetime import date


class Bot():
    def __init__(self):
        self.message = ''
        self.commands = 'about, help, funtranslate <message>, date, joke'
        self.ft_message = ''
        self.date = ''
        self.rand_joke = ''
    
    
    
    def about(self):
        self.message = "I am Awesome Bot! I can translate any sentence you want into leetspeak!"
        return self.message
        
    def helper(self):
        return self.commands
        
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
    command = arg[1]
    if command == "funtranslate":
        if len(arg) < 3:
            return "You forgot to enter what you wanted me to translate you silly goose!"
        text = arg[2:]
        t = ' '.join(text)
        return bot.funtranslate(t)
        
    elif command == "help":
        return bot.helper()
    elif command == "about":
        return bot.about()
    elif command == "date":
        return bot.dat()
    elif command == "joke":
        return bot.joke()
    else:
        return "Invalid command! Enter '!! help' to see available commands!"