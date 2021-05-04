# Prime Numbers
The function outputs all pairs of prime numbers found as tuples.

These must be in the form ``( ìsprime(i) , isprime(i+2))`` vorliegen. Wobei ``ìsprime`` immer true ist.
## Syntax
```Python
for i in range(1, 10000):
    if isprime(i) and isprime(i+2):
        prime_figures.append((i, i+2))
```
The function determines all prime twins and outputs them. However, the function is also to be extended.  

[Read more](/Prime_number)
