#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 13:10:17 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt

nVals = [100000]
colours = ['r', 'g', 'b'] # Colour Plots

G = 6.672e-11 # Gravitational Constant
M = 1.989e30 # Solar Mass

startTime = 0
endTime = 4e7

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

def SecondOrderRK(h, r0, t):
    k1 = h*VectorF(r0, t)
    k2 = h*VectorF(r0 + 0.5*k1, t + 0.5*h)
    r1 = r0 + k2
    return r1

for N in nVals:
    t = startTime
    x0 = 1.471e11
    y0 = 0
    vX0 = 0
    vY0 = 30.287e3
    r0 = [x0, y0, vX0, vY0]
    h = endTime/N
    tVals = np.linspace(startTime, endTime, N)
    rList = list()
    for t in tVals:
        r1 = SecondOrderRK(h, r0, t)
        rList.append(r1)
        r0 = r1
    rVals = np.array(rList).transpose()
    xVals = rVals[0]
    yVals = rVals[1]
    plt.plot(xVals, yVals, f'{colours[nVals.index(N)]}o', markersize = 1, label=f'y(x), N = {N}')
    np.delete(rVals, 4)

plt.title('Comet Orbit')
# plt.legend()
plt.plot(0, 0, 'o', color='gold')
plt.show()