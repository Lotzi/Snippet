# CodeSnippet
## GitCloner
The programme is a git administration programme. It clones all public repos from a specific user. 

```python
g = Github()
username = g.get_user(user)
repos = []
size = len("Repositoryfull_name") + 4 + len(user)
for repo in username.get_repos():
    repos.append(str(repo)[size:-2:])
for runner in repos:
    module = f"https://github.com/{user}/{runner}.git"
    Repo.clone_from(module, os.getcwd() + sub + runner)
```
[Read more](/GitCloner)

## Letter
This is a simple template for latex letters. 
You can use this template again and again.
- Download Artifacts: [Download PDF](https://github.com/Fennvel/CodeSnippet/actions/workflows/letter.yml)

[Read more](/Letter)

## Lichess Token 

This program searches by random values Lichess API Tokens.

```python
token_example = 'CB8YzDTrpSiqHV5l'
```
[Read more](/Lichess_Token)

###  Generating Keys
I simply use a string with all possible characters and create a substring from this set.

```python
def cheat_tokens():
    for i in range(0, len(token_example)):
        cheat_token = cheat_token + chars[random.randint(0, len(chars)-1)]

```

# MakeFile
I only use it to learn how MakeFiles work. 


```Makefile
SOURCE	= main.cpp 
all: $(OBJS)
	$(CC) -g $(OBJS) -o $(OUT) $(LFLAGS)
	del *.o

main.o: main.cpp
	$(CC) $(FLAGS) main.cpp --std=c++17
``` 

[Read more](/MakeFile)

## No_Commit_Runner

### Application
``` PowerShell
py.exe .\no_commit.py <<Read_File>> <<Write_File>>
```
It is necessary that both files exist.

## Pizza
With the API you can order a pizza at Dominos.  Quite funny, actually. 

### Syntax
```Python 
def create_address(adr, city, state, plz):
    return Address(adr, city, state, plz)
```
### RIP
Unfortunately, it seems that the API has been closed. This means that it can no longer be used. I deeply regret this. 

[Read more](/Pizza)

## PlayGround
Here we are just playing around with the Python GUI. 

```Python
# Import and initialize the pygame library
import pygame
pygame.init()
```

[Read more](/PlayGround)

## Prime Number

### Syntax
```Python
for i in range(1, 10000):
    if isprime(i) and isprime(i+2):
        prime_figures.append((i, i+2))
```
The function determines all prime twins and outputs them. However, the function is also to be extended.  

[Read more](/Prime_number)

## Square Number
Calculation of the difference of the square numbers.

### Example
```Log
(2,1)^2 --> (4,1) : 4 - 1  =  3
(3,2)^2 --> (9,4) : 9 - 4  =  5
(4,3)^2 --> (16,9) : 16 - 9  =  7
```
[Read more](/Square_Number)