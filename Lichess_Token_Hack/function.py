import requests
import lichess.api
import string
import random

# create Header
def create_header(token):
    user = user.lower()
    url = 'https://lichess.org/team/asdadasd/kick/HaterCheaterHater'
    header = {'Authorization': 'Bearer ' + token}
    return header

# create request
def create_request(header):
    return requests.post(url, headers=header)


# Analyse Request
def analyse(level):
    if "true" in level:
        return True
    return False

# No such token
def status(level):
    if "true" not in level.text: 
        # Wrong Key
        if "No such token" in level.text:
            return "No such token"
        # other Error
        return "Unknown Error"
    else:
        return "No Error" 

# Create cheat Token
def cheat_token(token_example):
    cheat_token = ''
    chars = ''
    
    for numbers in range(0, 10):
        chars = chars+str(numbers)

    for lowercase in string.ascii_lowercase:
        chars = chars+lowercase

    for uppercase in string.ascii_uppercase:
        chars = chars+uppercase
    
    try:
        for i in range(0, len(token_example)):
            cheat_token = cheat_token + chars[random.randint(0, len(chars)-1)]
    except:
        cheat_token = ''
        quit()

    return cheat_token

