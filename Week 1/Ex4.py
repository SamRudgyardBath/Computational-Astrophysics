#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:11:57 2023

@author: sam
"""
import numpy as np

# Define Constants
k = 1.380649e-23 # Boltzmann's Constant
h = 6.62607015e-34 # Planck's Constant
c = 3e8 # Speed of Light

def Integrand(x):
    if x == 0:
        return 0
    else:
        return (x**3)/(np.exp(x) -1)

def Integral():
    estimate = 0
    areaOfStrip = 1
    n = 0
    
    h = 0.1
    
    # for n in range(0, N+1):
    #     estimate += (Integrand(n*h) + Integrand((n+1)*h))/2 * h
        
    while areaOfStrip > 1e-15:
        areaOfStrip = (Integrand(n*h) + Integrand((n+1)*h))/2 * h
        estimate += areaOfStrip
        n += 1
    
    return estimate

u = (2 * np.pi * k**4) / (h**3 * c**2) * Integral()
print(f'u = {u}')