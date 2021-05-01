## Lichess Token 

This program searches by random values Lichess API Tokens.

### Example
Here is a simple example. For security purposes, this is invalid.

```python
token_example = 'CB8YzDTrpSiqHV5l'
```


### Creating the Keys
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


# MakeFile
I only use it to learn how MakeFiles work. 

## Latest version
I currently use the following version.

```Makefile
OBJS	= main.cpp
SOURCE	= main.cpp
HEADER	= 
OUT	= Test
CC	 = g++
FLAGS	 = -g3 -c -Wall
LFLAGS	 = 
# -g option enables debugging mode 
# -c flag generates object code for separate files


all: $(OBJS)
	$(CC) -g $(OBJS) -o $(OUT) $(LFLAGS)
	del *.o

Makefile: $(OBJS)
	$(CC) -g $(OBJS) -o $(OUT)

# create/compile the individual files >>separately<<
main.o: main.cpp
	$(CC) $(FLAGS) main.cpp --std=c++17


# clean house
clean:
	rm -f $(OBJS) $(OUT)

# run the program
run: $(OUT)
	./$(OUT)

# compile program with debugging information
debug: $(OUT)
	valgrind $(OUT)

# run program with valgrind for errors
valgrind: $(OUT)
	valgrind $(OUT)

# run program with valgrind for leak checks
valgrind_leakcheck: $(OUT)
	valgrind --leak-check=full $(OUT)

# run program with valgrind for leak checks (extreme)
valgrind_extreme: $(OUT)
	valgrind --leak-check=full --show-leak-kinds=all --leak-resolution=high --track-origins=yes --vgdb=yes $(OUT)
```

The Makefile compiles a *.exe file for me. However, I still don't understand how to compile Latex with it.
If you have any ideas, feel free to make an issue or request. 

## No_Commit_Runner

### Application
``` PowerShell
py.exe .\no_commit.py Datei_zum_Lesen Datei_zum_schreiben
```
It is necessary that both files exist.

### Example of files in the test folder

```PowerShell
py.exe .\no_commit.py .\test\test_commit.txt .\test\test_fertig.txt
```

### Output
The script always returns the deleted lines.

```PowerShell
Delete: # Hallo Welt
```

### New file format

New file formats can be added in database.py.

# PlayGround
Here we are just playing around with the Python GUI. 

```Python
# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
```

# Squere Number

Calculation of the difference of the square numbers.