#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:54:12 2023

@author: sam
"""
import numpy as np
import matplotlib.pyplot as plt

def Dxdt(x, t):
    return np.sin(t) - x**3

nVals = [100, 1000, 10000, 100000]
colours = ['r', 'g', 'b', 'k']

xVals = list()

def EulerMethod():
    for N in nVals:
        tVals = np.linspace(0, 10, N)
        x0 = 0
        h = 10/N
        for t in tVals:
            x1 = x0 + h*Dxdt(x0, t)
            xVals.append(x1)
            x0 = x1
        plt.plot(tVals, xVals, colours[nVals.index(N)], label=f'N = {N}')
        xVals.clear()
    
EulerMethod()
plt.title('Eulers Method')
plt.legend()
plt.show()