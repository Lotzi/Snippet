# Lichess Token 

This program searches by random values Lichess API Tokens.

## Example
This program searches by random values Lichess API Tokens.

```python
token_example = 'CB8YzDTrpSiqHV5l'
```


## Creating the Keys
I simply use a string with all possible characters and create a substring from this set.

```python
def cheat_tokens(token_example):
    cheat_token = ''
    chars = ''
    
    for numbers in range(0, 10):
        chars = chars+str(numbers)

    for lowercase in string.ascii_lowercase:
        chars = chars+lowercase

    for uppercase in string.ascii_uppercase:
        chars = chars+uppercase

    for i in range(0, len(token_example)):
        cheat_token = cheat_token + chars[random.randint(0, len(chars)-1)]

```

These are then tested through a continuous loop. 