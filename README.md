# CodeSnippet
## Lichess Token 

This program searches by random values Lichess API Tokens.

```python
token_example = 'CB8YzDTrpSiqHV5l'
```
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

## No_Commit_Runner

### Application
``` PowerShell
py.exe .\no_commit.py <<Datei_zum_Lesen>> <<Datei_zum_schreiben>>
```
It is necessary that both files exist.


## PlayGround
Here we are just playing around with the Python GUI. 

```Python
# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
```

## Square Number
Calculation of the difference of the square numbers.

### Example
```Log
(2,1)^2 --> (4,1) : 4 - 1  =  3
(3,2)^2 --> (9,4) : 9 - 4  =  5
(4,3)^2 --> (16,9) : 16 - 9  =  7
```
