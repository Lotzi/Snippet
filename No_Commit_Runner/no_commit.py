import sys
import re

# Path_to_read [1]
# Path_to_write [2]

x = len(sys.argv[1])

while x > 0:
    if "." in sys.argv[1][-x::]:
        x = x - 1
        print(sys.argv[1][-x::])
    else:
        Trennzeichen = sys.argv[1][-x::]
        break


if x == "py":
    Trennzeichen = "#"
elif x == "pgn":
    Trennzeichen = "%"
elif x == "java":
    Trennzeichen = "//"
elif x == "text":
    Trennzeichen = "#"
else:
    print("Unbekanntes Format")
    quit()

file_read = open(sys.argv[1], "r+")
file_write = open(sys.argv[2], "r+")


for line in file_read:
    if sys.argv[3] in line:
        print("Delete: "+line)
    else:
        file_write.write(line)

file_read.close()
file_write.close()