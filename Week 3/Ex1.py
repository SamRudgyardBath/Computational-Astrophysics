#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:18:22 2023

@author: sam
"""
import numpy as np
import matplotlib.pyplot as plt

r0 = np.array([0, float(50)]) # [z, v]
g = -9.81
startTime = 0; endTime = 10
N = 100
delta = 1
h = (endTime - startTime)/N
tVals = np.linspace(startTime, endTime, N)
rVals = list()

def Velocity(r, t):
    return r[1]

def Acceleration(r, t):
    return g

def VectorF(r, t):
    v = Velocity(r, t)
    a = Acceleration(r, t)
    return np.array([v, a])

def FourthOrderRK(h, r0, t):
    k1 = h*VectorF(r0, t)
    k2 = h*VectorF(r0 + 0.5*k1, t + 0.5*h)
    k3 = h*VectorF(r0 + 0.5*k2, t + 0.5*h)
    k4 = h*VectorF(r0 + k3, t + h)
    r1 = r0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    return r1

def FindFinalDisp(r0): # Calculate the z displacement of the ball at t=10s
    rVals.clear()
    for t in tVals:
        rVals.append(r0)
        r1 = FourthOrderRK(h, r0, t)
        r0 = r1
    return np.array([r0[0], r0[1]])

def ApproxChange(r0): # Gradient of the initial velocity - final displacement at the point of consideration
    return 1/h * (FindFinalDisp([r0[0], r0[1] + h]) - FindFinalDisp(r0)) # Adjust the initial velocity  by h, but not the initial displacement

while abs(delta) > 1e-12:
    print(f' Starting Velocity = {r0[1]}')
    finalDisp = FindFinalDisp(r0)
    approxChange = ApproxChange(r0)
    delta = - finalDisp[0]/approxChange[0]
    r0[1] += delta
    
rArray = np.array(rVals).transpose()

plt.plot(tVals, rArray[0], 'b', label='Position')
plt.plot(tVals, rArray[1], 'r', label='Velocity')

print(f'Value of z at t=10 is {finalDisp[0]}, delta = {delta}')
    