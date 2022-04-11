# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import sympy
import math

def symmetric_derivative(x):
    h = 1e-5
    return (fun(x+h)-fun(x-h))/(2*h)

def definition_derivative(x):
    h = 1e-5
    return (fun(x+h)-fun(x))/(h)

def fun(x):
    return x**2 - 1

def fun2D(x,y):
    return 2*x**2 + y**2 - 1

def gradient2D(x,y):
    h = 1e-5
    t1 = (fun2D(x+h,y)-fun2D(x-h,y))/(2*h)
    t2 = (fun2D(x,y+h)-fun2D(x,y-h))/(2*h)
    return np.array([t1, t2])

print(math.sqrt(8))
print(sympy.sqrt(8))

x,y = sympy.symbols('x y')
expr = x*(x+2*y)
expanded_expr = sympy.expand(expr)
fact_expr = sympy.factor(expanded_expr)
print(expr) 
print(expanded_expr)
print(fact_expr)

def newton_raphson(x):
    x2 = x - fun(x)/symmetric_derivative(x)
    print(x2)
    for a in range(0,20):
        x2 = x2 - fun(x2)/symmetric_derivative(x2)
        print(x2)
        if x2-x < 1e-5:
            return x2
        
def newton_raphson2(x):
    x2 = x - fun(x)/definition_derivative(x)
    print(x2)
    for a in range(0,20):
        x2 = x2 - fun(x2)/definition_derivative(x2)
        print(x2)
        if x2-x < 1e-5:
            return x2
        
def sekant(x0,x1):
    x2 = x1 - (x1-x0)/(fun(x1)-fun(x0))*fun(x1)
    x3 = x1 - (x1-x0)/(fun(x1)-fun(x0))*fun(x1)
    print(x2)
    for a in range(0,20):
        x2 = x2 - fun(x2)/definition_derivative(x2)
        print(x2)    
        
def trapets_integral(a,b,N):
    h = (b-a)/N
    integral = 0
    for k in range(0,N):
        integral += h*(fun(a+k*h)+fun(a+k*h+h))/2
    print(integral)
        
    
#t = newton_raphson(33)
#print(t)

#u = sekant(33,35)
#print(u)
    
#w = trapets_integral(1,2,120)