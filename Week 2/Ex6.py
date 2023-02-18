#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:10:08 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt

nVals = [10, 100, 1000]
colours = ['r', 'g', 'b'] # Colour Plots

G = 6.672e-11 # Gravitational Constant
M = 1.989e30 # Solar Mass

startTime = 0
endTime = 1.5e9

tolerance = 1e-6

def Velocity(r, t): # dr/dt
    vX = r[2]
    vY = r[3]
    return [vX, vY]
    
def Acceleration(r, t): # dv/dt
    rX = r[0]
    rY = r[1]
    rVec = np.array([rX, rY])
    rMag = np.sqrt(rX**2 + rY**2)
    
    return -(G*M)/(rMag**2) * rVec/rMag

def VectorF(r, t):
    v = Velocity(r, t)
    a = Acceleration(r, t)
    return np.array([v[0], v[1], a[0], a[1]])

def FourthOrderRK(h, r0, t):
    k1 = h*VectorF(r0, t)
    k2 = h*VectorF(r0 + 0.5*k1, t + 0.5*h)
    k3 = h*VectorF(r0 + 0.5*k2, t + 0.5*h)
    k4 = h*VectorF(r0 + k3, t + h)
    r1 = r0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    return r1

for N in nVals:
    t = startTime
    x0 = 5.2e12
    y0 = 0
    vX0 = 0
    vY0 = 880
    r0 = [x0, y0, vX0, vY0]
    h = endTime/N
    rList = list()
    while t < endTime:
        r1 = FourthOrderRK(h, r0, t)
        doubleStepR = FourthOrderRK(h, r1, t)
        singleStepR = FourthOrderRK(2*h, r0, t)
        doubleStepV = np.sqrt(doubleStepR[2]**2 + doubleStepR[3]**2)
        singleStepV = np.sqrt(singleStepR[2]**2 + singleStepR[3]**2)
        error = 1/30 * abs(doubleStepV - singleStepV) # Eqn 20 in Lecture 2 Notes
        if error > tolerance:
            h *= (tolerance / error)**(1/5) # Optimal value of h
        elif error < tolerance: # Only increase the time step when error is less than that required
            h *= (tolerance / error)**(1/5)
            rList.append(doubleStepR)
            r0 = doubleStepR
            t += h
    rVals = np.array(rList).transpose()
    xVals = rVals[0]
    yVals = rVals[1]
    plt.plot(xVals, yVals, f'{colours[nVals.index(N)]}o', markersize = 1, label=f'y(x), N = {N}')
    np.delete(rVals, 4)

plt.title('Comet Orbit')
plt.legend()
plt.plot(0, 0, 'o', color='gold')
plt.show()