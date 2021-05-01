
# List of all positive integers from 0 to n
figure = range(2, 101)

# List of all square numbers from the figures array.
squere = []

# Generates the list of square numbers
for i in figure:
    squere.append(i**2)

# Maths output for lazy people
symbol = '²'

for i in figure:
    # When the array is finished, the programme terminates.
    # Then there is no annoying error message
    try:
        dummy = squere[i]
    except:
        quit()

    # Template for the output
    calc = squere[i]-squere[i-1]

    # The tuple consists of the entered numbers.
    tuple_figure = "(" + str(i) + "," + str(i - 1) + ")"+symbol+" -->"
    tuple_squere = "(" + str(i**2) + "," + str((i - 1)**2) + ") :"

    # Generates the output for the console
    diff = squere[i] - squere[i-1]
    tuple_ausgabe = str(squere[i])+" - "+str(squere[i-1])

    # Output
    print(tuple_figure, tuple_squere, tuple_ausgabe, " = ", diff)
