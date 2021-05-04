# Imports
from function import check_is_prime as isprime

# List of prime numbers
prime_figures = []

# List of Prime Tuples
for i in range(1, 10000):
    if isprime(i) and isprime(i+2):
        prime_figures.append((i, i+2))

# Output
for x in prime_figures:
    print(str(x)+";",  end=" ")
