#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:46:24 2023

@author: sam
"""
import numpy as np
import matplotlib.pyplot as plt

nVals = [1000]

omega = 1

def Dxdt(r, t):
    y = r[1]
    return y
    
def Dydt(r, t):
    x = r[0]
    return -omega**2 * x

def fVector(r, t):
    dxdt = Dxdt(r, t)
    dydt = Dydt(r, t)
    return np.array([dxdt, dydt])

def FourthOrderRK():
    for N in nVals:
        tVals = np.linspace(0, 50, N)
        x0 = 1
        dxdt0 = 0
        r0 = [x0, dxdt0]
        h = 50/N
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
        plt.plot(tVals, rVals[0], 'k', label='x(t)')
        np.delete(rVals, 2)
        
FourthOrderRK()
plt.title('Simple Harmonic Oscillator')
plt.legend()
plt.show()