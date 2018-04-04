#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
""" desafio 4

    Pedro Tomaz Alves 2018-04-03
    
    
""" 


import itertools
izip = itertools.zip_longest
chain = itertools.chain.from_iterable
compress = itertools.compress
def rwh_primes2_python3(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    zero = bytearray([False])
    size = n//3 + (n % 6 == 2)
    sieve = bytearray([True]) * size
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        start = (k*k+4*k-2*k*(i&1))//3
        sieve[(k*k)//3::2*k]=zero*((size - (k*k)//3 - 1) // (2 * k) + 1)
        sieve[  start ::2*k]=zero*((size -   start  - 1) // (2 * k) + 1)
    ans = [2,3]
    poss = chain(izip(*[range(i, n, 6) for i in (1,5)]))
    ans.extend(compress(poss, sieve))
    return ans
    

frase = "ILM runs a batch processing environment capable of modeling rendering and compositing tens of thousands of motion picture frames per day" 

for letters in [x for x in frase.split(' ')]:
    print(f'\n{letters} ', end='')
    numero = 0
    for letter in letters:
        # Get number that represents letter in ASCII.
        number = ord(letter)
        if  number < 96:   
            saida = number - 38
        else:
            saida = number - 96
        numero += saida
    primos = rwh_primes2_python3(numero+1)
    if numero in primos:
        print('é primo', end='')
        
