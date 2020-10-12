import requests
from datetime import date


name = "Awesome Bot"
commands = ["about", "help", "funtranslate <message>", "date","joke"]


def switch(arg):
    command = arg[1]
    if command == "funtranslate":
        if len(arg) < 3:
            return "You forgot to enter what you wanted me to translate you silly goose!"
        text = arg[2:]
        t = ' '.join(text)
        return funtranslate(t)
        
    elif command == "help":
        return helper()
    elif command == "about":
        return about()
    elif command == "date":
        return dat()
    elif command == "joke":
        return joke()
    else:
        return "Invalid command! Enter '!! help' to see available commands!"


def about():
    message = "I am an awesome bot! I have the ability to use funtranslate to translate any sentence you want into leetspeak!"
    return message
    
def helper():
    com = "Here is a list of commands I understand: " + ', '.join(commands)
    return com
    
def funtranslate(text):
    base = "https://api.funtranslations.com/translate/leetspeak.json?text=" + text
    req = requests.get(base)
    respo = req.json()
    f = respo['contents']['translated']
    return f
    
def dat():
    today = date.today()
    d = "Today's date is " + str(today)
    return d
    
    
def joke():

    url = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "6bd46d61f2mshd2c80482e12a730p16f242jsn3b38dc8f3fb4",
        }
    
    response = requests.request("GET", url, headers=headers)
    
    return response.text