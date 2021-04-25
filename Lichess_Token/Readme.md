# Lichess Token 

Dieses Programm sucht durch Zufalls Werte Lichess API Tokens

## Example
Hier ein einfaches Beispiel. Zu Sicherheitszwecken ist dieser Ungültig

```python
token = 'CB8YzDTrpSiqHV5l'
```
https://github.com/Zeyecx/CodeSnippet/blob/20c755e90c490ee85a9642f056d2ff3233a5d002/Lichess_Token/main.py#L4

## Generierung
Ich nutze einfach einen String mit allen möglichen Zeichen und bastel mir einen dummy String

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