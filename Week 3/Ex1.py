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
