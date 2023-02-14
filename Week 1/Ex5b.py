#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:45:59 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt

def Integrand(m, x, theta):
    return np.cos(m*theta -x*np.sin(theta))

def J(m, x):
    estimate = 0
    
    N = 10000
    h = np.pi/(N-1)
    for n in range(0, N+1):
        estimate += (Integrand(m, x, n*h) + Integrand(m, x, (n+1)*h))/2 * h
    
    return estimate

rVals = np.linspace(-25, 25, 100)
j1Vals = list()
intensityVals = list()

for r in rVals:
    x = np.pi * r/5.1
    j = J(1, x)
    j1Vals.append(j)
    intensityVals.append((2*j/x)**2)
    
    
plt.plot(rVals, intensityVals, 'k')

