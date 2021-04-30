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