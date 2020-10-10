import requests


name = "Awesome Bot"
commands = ["about", "help", "funtranslate <message>", "date","joke"]


def switch(arg):
    command = arg[1]
    if command == "funtranslate":
        if len(arg) < 3:
            return "You forgot to enter what you wanted me to translate you silly goose!"
        text = str(arg[2:])
        funtranslate(text)
        
    if command == "help":
        helper()
        
    if command == "about":
        about()
    return


def about():
    message = "I am an awesome bot! I have the ability to use funtranslate to translate any sentence you want into leetspeak!"
    print(message)
    
def helper():
    print("Here is a list of commands I understand: ")
    print (', '.join(commands))
    
def funtranslate(text):
    base = "https://api.funtranslations.com/translate/leetspeak.json?text=" + text
    req = requests.get(base)
    respo = req.json()
    print(respo)
    print(respo['contents']['translated'])
    
