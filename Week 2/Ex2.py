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

nVals = [20, 50, 200]

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
        plt.plot(tVals, xVals, 'r', label=f'Euler, N = {N}')
        xVals.clear()

def SecondOrderRK():
    for N in nVals:
        tVals = np.linspace(0, 10, N)
        x0 = 0
        h = 10/N
        for t in tVals:
            k1 = h*Dxdt(x0, t)
            k2 = h*Dxdt(x0 + 0.5*k1, t + 0.5*h)
            x1 = x0 + k2
            xVals.append(x1)
            x0 = x1
        plt.plot(tVals, xVals, 'g', label=f'RK2, N = {N}')
        xVals.clear()
        
def FourthOrderRK():
    for N in nVals:
        tVals = np.linspace(0, 10, N)
        x0 = 0
        h = 10/N
        for t in tVals:
            k1 = h*Dxdt(x0, t)
            k2 = h*Dxdt(x0 + 0.5*k1, t + 0.5*h)
            k3 = h*Dxdt(x0 + 0.5*k2, t + 0.5*h)
            k4 = h*Dxdt(x0 + k3, t + h)
            x1 = x0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
            xVals.append(x1)
            x0 = x1
        plt.plot(tVals, xVals, 'b', label=f'RK4, N = {N}')
        xVals.clear()

EulerMethod()
SecondOrderRK()
FourthOrderRK()
plt.title('Comparison of Euler, RK2 and RK4')
plt.legend()
plt.show()