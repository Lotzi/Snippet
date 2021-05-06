# Nesting Level

test = "(2+3)-3(+32ßa)"

bracket = [0, 0]
nest = []
length = len(test)

for i in test:
    if i == "(":
        bracket[0] = bracket[0] + 1
    if i == ")":
        bracket[1] = bracket[1] + 1

if bracket[1] != bracket[0]:
    print("Wrong Syntax")
    quit

for x in test:
    nest.append(0)

i = 0
sig = 0

for y in test:
    if i != 0:
        nest[i] = nest[i-1]
    if y == "(":
        sig = sig + 1
        nest[i] = nest[i] + 1
    elif y == ")":
        nest[i] = nest[i] - 1
    i = i + 1

minimum = sorted(nest)[0]
maximum = sorted(nest)[len(nest)-1]


print("Nesting Regular expression")
print("expression: ", test)
print("Maximum: ", maximum)
print("Minimum: ", minimum)
print("tiefster Punkt: \n Zeichen:", test[sig-1],"\n Position:",str(sig-1))
