#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:23:35 2023

@author: sam
"""
import numpy as np
import matplotlib.pyplot as plt

def integrand(t):
    return np.exp(-t**2)

def E(x, N):
    estimate = 0
    
    h = x/(N-1)
    for n in range(0, N+1):
        estimate += (integrand(n*h) + integrand((n+1)*h))/2 * h
    
    return estimate

eVals = list()
h = 1e-14
N = 1000

xVals = np.linspace(0, 3, num = 31)

for x in xVals:
    eVals.append(E(x, N))
    
plt.plot(xVals, eVals)