import sys
import re
from database import getTrennzeichen as gT


# Path_to_read [1]
# Path_to_write [2]

x = len(sys.argv[1])

while x > 0:
    if "." in sys.argv[1][-x::]:
        x = x - 1
    else:
        File_Format = sys.argv[1][-x::]
        break

if gT(File_Format) == False:
    print("Unbekanntes Format")
    quit()
 
Trennzeichen = gT(File_Format)

file_read = open(sys.argv[1], "r+")
file_write = open(sys.argv[2], "r+")


for line in file_read:
    if Trennzeichen in line:
        print("Delete: "+line)
    else:
        file_write.write(line)

file_read.close()
file_write.close()