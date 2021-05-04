# Imports
from function import check_is_prime as isprime
import sys

# set max
cap = sys.maxsize

# List of Prime Tuples
for i in range(1, 1000000, 1):
    
    # Architecture 1
    if isprime(i) and isprime(i+2) and isprime(i+6):
        print((i, i+2, i+6))

    # Architecture 2
    if isprime(i) and isprime(i+4) and isprime(i+6):
        print((i, i+4, i+6))