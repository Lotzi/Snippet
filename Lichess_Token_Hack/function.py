import requests
import lichess.api
import string

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
def analyse(request_socket):
    if "true" in request_socket:
        return True
    return False


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

    for i in range(0, len(token_example)):
        cheat_token = cheat_token + chars[random.randint(0, len(chars))]

    return cheat_token
