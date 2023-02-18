#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:43:56 2023

@author: sam
"""
import numpy as np
import matplotlib.pyplot as plt

nVals = [50, 100, 1000]

alpha = 1
beta = gamma = 0.5
delta = 2

def Dxdt(r, t):
    x = r[0]
    y = r[1]
    return alpha*x - beta*x*y

def Dydt(r, t):
    x = r[0]
    y = r[1]
    return gamma*x*y - delta*y

def fVector(r, t):
    dxdt = Dxdt(r, t)
    dydt = Dydt(r, t)
    return np.array([dxdt, dydt])

def FourthOrderRK():
    for N in nVals:
        tVals = np.linspace(0, 30, N)
        r0 = [2, 2]
        h = 30/N
        rList = list()
        for t in tVals:
            k1 = h*fVector(r0, t)
            k2 = h*fVector(r0 + 0.5*k1, t + 0.5*h)
            k3 = h*fVector(r0 + 0.5*k2, t + 0.5*h)
            k4 = h*fVector(r0 + k3, t + h)
            r1 = r0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
            rList.append(r1)
            r0 = r1
        rVals = np.array(rList).transpose()
        plt.plot(tVals, rVals[0], 'b', label=f'x (rabbits), N = {N}')
        plt.plot(tVals, rVals[1], 'r', label=f'x (foxes), N = {N}')
        np.delete(rVals, 2)
        
FourthOrderRK()
plt.title('Population of Rabbits and Foxes')
plt.legend()
plt.show()