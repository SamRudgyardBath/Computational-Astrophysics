#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:46:24 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt

m0 = np.array([5e8, 0]) # [rho, m], central density and mass

G = 6.672e-11 # Gravitational Constant
gamma = 5/3
K = 3e6
h = 100
r0 = 0 # Initial radius of zero
rVals = list(); rVals.append(r0)
mVals = list(); mVals.append(m0)

def GradDensity(m, r):
    density = m[0]
    mass = m[1]
    if density < 0: # Density can be -ve for RK4 when close to surface, causing numpy to give a warning
        densityTerm = np.sign(density) * (np.abs(density))**(2 - gamma)
        return - (G * mass * densityTerm)/(gamma * K * r**2)
    return - (G * mass * density**(2 - gamma))/(gamma * K * r**2)

def GradMass(m, r):
    density = m[0]
    return 4 * np.pi * density * r**2

def VectorF(m, r):
    deltaRho = GradDensity(m, r)
    deltaM = GradMass(m, r)
    return np.array([deltaRho, deltaM])

def FourthOrderRK(h, m0, r):
    k1 = h*VectorF(m0, r)
    k2 = h*VectorF(m0 + 0.5*k1, r + 0.5*h)
    k3 = h*VectorF(m0 + 0.5*k2, r + 0.5*h)
    k4 = h*VectorF(m0 + k3, r + h)
    m1 = m0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    return m1

while m0[0] > 1:
    r0 += h
    m1 = FourthOrderRK(h, m0, r0)
    rVals.append(r0)
    mVals.append(m1)
    m0 = m1
    
print(f'Mass of the white dwarf is {m0[1]:2e} kg, or {(m0[1]/1.989e30):2e} Solar Masses')

densityVals = np.array(mVals).transpose()[0]
massVals = np.array(mVals).transpose()[1]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Radius')
ax1.set_ylabel('Density', color = 'b')
ax1.plot(rVals, densityVals, 'b')

ax2 = ax1.twinx() # Share the same x-axis
ax2.set_ylabel('Mass', color = 'r')
ax2.plot(rVals, massVals, 'r')

plt.show()