#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:19:40 2023

@author: sam
"""

def Factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def Exp(x, noTerms):
    approx = 1
    for i in range(1, noTerms - 1):
       approx += x**i / Factorial(i)
    return approx

x = int(input('Estimate exp(x) for x = '))
noTerms = int(input('Number of terms: '))

print(f'exp({x}) = {Exp(x, noTerms)}')