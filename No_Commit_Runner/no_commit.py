
Path_to_read = "test_commit.txt"
Trennzeichen = "#"
Path_to_write = "test_fertig.txt"


file_read = open(Path_to_read, "r+")
file_write = open(Path_to_write, "r+")


for line in file_read:
    if Trennzeichen in line:
        print("Delete: "+line)
    else: 
        file_write.write(line) 

file_read.close()
file_write.close()