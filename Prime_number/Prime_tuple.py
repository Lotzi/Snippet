# Imports
from function import check_is_prime as isprime
import sys

# set max
cap = sys.maxsize

# List of prime numbers
prime_figures = []

# List of Prime Tuples
for i in range(1, cap, 1):
    if isprime(i) and isprime(i+3):
        prime_figures.append((i, i+3))

# Output
for x in prime_figures:
    print(str(x)+";",  end=" ")
