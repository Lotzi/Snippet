start = 1
ende = 100

diff = []

# Legt die Liste an
for x in range(0,100):
    d =(x+1)**2 - x**2
    diff.append(d)


# Test
for y in diff:
    print(y)