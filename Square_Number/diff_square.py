import sys

# Error Handling 
error = False

# Testing for control arguments
try:
    if len(sys.argv) == 3:
        # Convert the arguments into numbers
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        # Test the numbers        
        if start > end:
            error = True
            print("Start must be smaller than the end.")
        
except:
    # If there are no control arguments, basic values are taken. 
    start = 1
    end = 1001

# Error Exit
if error:
    print("Error")
    quit()

# List of all positive integers from 0 to n
figure = range(start, end)

# List of all square numbers from the figures array.
square = []

# Generates the list of square numbers
for i in figure:
    square.append(i**2)

# Maths output for lazy people
symbol = '^2'

for i in figure:
    # When the array is finished, the programme terminates.
    # Then there is no annoying error message
    try:
        dummy = square[i]
    except:
        quit()

    # The tuple consists of the entered numbers.
    tuple_figure = "(" + str(i) + "," + str(i - 1) + ")"+symbol+" -->"
    tuple_square = "(" + str(i**2) + "," + str((i - 1)**2) + ") :"

    # Generates the output for the console
    diff = square[i-1] - square[i-2]
    tuple_ausgabe = str(square[i-1])+" - "+str(square[i-2])

    # Output
    if diff > 0:
        print(tuple_figure, tuple_square, tuple_ausgabe, " = ", diff)
