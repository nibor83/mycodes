# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:02:32 2020

@author: robin
"""
import numpy as np
import sympy as sp
import scipy.optimize as scp
import matplotlib.pyplot as plt
import pandas as pd

#Settings
initial_xvalue = -5 #Initial guess for the x-value
max_iter = 400 #Maximum number of iterations in the solver
myfunction = 'x**3 + x - 1' #Function under consideration
myfunctionder = '3*x + 1' #Derivative of the function (for the built in Scipy solver)

array_newton_x = [] #Contains the x-values from the solver
array_newton_y = [] #Contains the y-values from the solver
previous_x = 0 #The previous x-value, used for defining a cutoff accuracy

def symmetric_derivative(x):
    h = 1e-5
    return (fun(x+h)-fun(x-h))/(2*h)

def newton_raphson(x):
    global array_newton_x
    global array_newton_y
    global max_iter
    global previous_x
    array_newton_x.append(x)
    array_newton_y.append(eval(myfunction))
    x = x - fun(x)/symmetric_derivative(x)
    array_newton_x.append(x)
    array_newton_y.append(eval(myfunction))
    for a in range(0,max_iter):
        previous_x = x
        x = x - fun(x)/symmetric_derivative(x)
        array_newton_x.append(x)
        array_newton_y.append(eval(myfunction))
        if abs(x-previous_x) < 1e-7:
            return x
        elif a == (max_iter-1):
            return x
        
def fun(x):
    global myfunction
    t = eval(myfunction)
    return t

def fun_der(x):
    global myfunctionder
    t = eval(myfunctionder)
    return t

print("Function under consideration: " + myfunction)

#My own Newton-Raphson method
t = newton_raphson(initial_xvalue)
print("My Newton-Raphson: " + str(t))
print("Iterations needed: " + str(int(len(array_newton_x))-1))

#Using the built in equation solver in Sympy
x = sp.symbols('x')
u = sp.solve(x**2 + x - 1)
print(type(u))
print("Sympy solve routine: " + str(u[0].evalf()) + " " + str(u[1].evalf()))

#Plotting the function
x = np.linspace(-10, 2, 400)
plt.plot(x, eval(myfunction), label=myfunction.replace('**', '^'))
plt.plot(array_newton_x, array_newton_y, 'ro', label='Newton-Raphson method, ' + str(int(len(array_newton_x))-1) + " iterations")
plt.legend()
plt.show()

#Using the built in newton method in Scipy
z = initial_xvalue
w = scp.newton(fun, 3, fun_der, tol=1e-7, maxiter=max_iter)
print("Scipy newton solver " + str(w))