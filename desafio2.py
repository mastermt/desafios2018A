#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
""" desafio 2

    Pedro Tomaz Alves 2018-04-03
    
    
""" 

from random import randint

lista1 = [randint(0,5000000) for x in range(500)]
lista2 = [randint(0,5000000) for x in range(50000)]

listafinal = [x for x in lista2 if x in lista1]

for item in listafinal:
    print(item)

