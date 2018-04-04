#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
""" desafio 3

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
    
    
while True:
    try:
        numero = int(input("\nIndique um número (0 para sair): "))
    except ValueError:
        print("\nErro: o valor digitado não é um número!")
        numero = 0
    if numero == 0:
        break
    
    print(f"\nLista de números primos ate '{numero}':\n")
    lista = rwh_primes2_python3(numero+1)
    for item in lista:
        print(f"{item}", end='-')