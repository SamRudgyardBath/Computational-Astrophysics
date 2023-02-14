#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:34:36 2023

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

xVals = np.linspace(0, 20)
j0Vals = list()
j1Vals = list()
j2Vals = list()

for x in xVals:
    j0Vals.append(J(0, x))
    j1Vals.append(J(1, x))
    j2Vals.append(J(2, x))
    

plt.plot(xVals, j0Vals, 'r')
plt.plot(xVals, j1Vals, 'g')
plt.plot(xVals, j2Vals, 'b')