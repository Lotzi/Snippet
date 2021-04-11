from function import *

# example Token
token_example = 'CB8YzDTrpSiqHV5l'

# Test
for i in range(10000):
# while True:

    # create Cheat Token
    cheat_token = cheat_tokens(token_example)

    # create Request 
    level = create_request(create_header(cheat_token))

    # Tester 
    sample = [] 
    if status(level) != "No such token":
        # Token true
        print(cheat_token+" --> True")
        sample.append(cheat_token)
    else:
        # Token false
        print(cheat_token+" --> False")

    #cheat_token = None

print("True Tokens:")
for x in range(0,len(sample)):
    print(sample[x])
    
