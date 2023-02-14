#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:35:36 2023

@author: sam
"""

def P(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

def dPdx(x, h):
    return 1/h * (P(x + h) - P(x))


estX = 0.8
h = 1e-14
delta = 1

while abs(delta) > 1e-10:
    delta = -P(estX)/dPdx(estX, h)
    estX += delta

print(estX)