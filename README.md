## Lichess Token 

Dieses Programm sucht durch Zufalls Werte Lichess API Tokens

### Example
Hier ein einfaches Beispiel. Zu Sicherheitszwecken ist dieser ungültig

```python
token_example = 'CB8YzDTrpSiqHV5l'
```


### Generierung
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

Durch eine Dauerschleife werden diese dann getestet. 


# MakeFile
Ich nutze das eig nur um zu lernen wie MakeFiles funktionieren. 

## Aktuelle Version
Aktuell nutze ich folgende Version.

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

Folgendes baut mir eine *.exe Datei. Allerdings verstehe ich es immer noch nicht, wie man damit Latex compilieren kann.
Wer Ideen hat, kann gerne ein Issue oder Request machen. 

## No_Commit_Runner

### Anwendung
``` PowerShell
py.exe .\no_commit.py Datei_zum_Lesen Datei_zum_schreiben
```
Es ist notwendig, dass beide Datein existieren.

### Beispiel an Datein im Ordner test

```PowerShell
py.exe .\no_commit.py .\test\test_commit.txt .\test\test_fertig.txt
```

### Output
Das Skript gibt immer die gelöschten Zeilen zurück.

```PowerShell
Delete: # Hallo Welt
```

### Neues Dateiformat

Neue Dateiformate können in der database.py nachgetragen werden.

# PlayGround
Hier wird einfach nur mit der Python GUI rumgespielt 

```Python
# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
```

# Squere Number

Berechnung der Differenz der Quadratzahlen.