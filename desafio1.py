#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
""" desafio 1

    Pedro Tomaz Alves 2018-04-03
    
    
""" 

lista = [x for x in range(1,301)]


while True:
    try:
        numero = int(input("\nIndique um número (0 para sair): "))
    except ValueError:
        print("\nErro: o valor digitado não é um número!")
        numero = 0
    if numero == 0:
        break
    
    indice = [indice for indice,retorno in enumerate(lista) if retorno==numero]
    if indice:
        print(f"\nO número '{numero}' foi localizado em {indice[0]}")
    else:
        print(f"\nO número '{numero}' não foi localizado na lista")