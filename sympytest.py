# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 05:09:45 2020

@author: robin
"""

import numpy as np
import sympy as sp
import scipy as scp
import matplotlib.pyplot as plt
import pandas as pd

def func(x):
    return x**2 + 1

def func2D(x,y):
    return x**2 + 2*y + 1

def gradient2D_symbolic(expr):
    t1 = sp.diff(expr, x)
    t2 = sp.diff(expr, y)
    t3 = np.array([t1, t2])
    return t3

x,y=sp.symbols('x y')
expr = x**2 + 3*y + 1

t = gradient2D_symbolic(expr)
print(t)

u = t[0].subs(x, 3)
print(u)

fig = plt.figure()
fig.suptitle('No axes on this figure')

fig, ax_lst = plt.subplots(2, 2)

plt.show()

a = pd.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asarray = a.values
print(a_asarray)

