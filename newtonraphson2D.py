# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:06:15 2020

@author: robin
"""

import numpy as np
import sympy as sp
import scipy.optimize as scp
import matplotlib.pyplot as plt
import pandas as pd

from mpl_toolkits import mplot3d

#Settings
step_size = 0.1 #Scaling constant for the gradient to determine step size
initial_xvalue = -5 #Initial guess for the x-value
initial_yvalue = -5 #Initial guess for the x-value
max_iter = 400 #Maximum number of iterations in the solver
myfunction = 'x**2 + y**2 - 1' #Function under consideration
#myfunctionder = '3*x + 1' #Derivative of the function (for the built in Scipy solver)

array_newton_x = [] #Contains the x-values from the solver
array_newton_y = [] #Contains the y-values from the solver
array_newton_z = [] #Contains the z-values from the solver
previous_x = 0 #The previous x-value, used for defining a cutoff accuracy
previous_y = 0 #The previous y-value, used for defining a cutoff accuracy

def symmetric_derivativex(x,y):
    h = 1e-5
    return (fun(x+h,y)-fun(x-h,y))/(2*h)

def symmetric_derivativey(x,y):
    h = 1e-5
    return (fun(x,y+h)-fun(x,y-h))/(2*h)

def fun(x,y):
    global myfunction
    t = eval(myfunction)
    return t

def fun2(x,y):
    return x**2 + y**2 - 1

def newton_raphson(x,y):
    global array_newton_x
    global array_newton_y
    global array_newton_z
    global max_iter
    global previous_x
    global previous_y
    global step_size
    array_newton_x.append(x)
    array_newton_y.append(y)
    array_newton_z.append(eval(myfunction))
    dfdx = fun(x,y)/symmetric_derivativex(x,y)
    dfdy = fun(x,y)/symmetric_derivativey(x,y)
    gradient = np.array([dfdx,dfdy])
    x = x - step_size*dfdx
    y = y - step_size*dfdy
    for a in range(0,max_iter):
        previous_x = x
        previous_y = y
        dfdx = fun(x,y)/symmetric_derivativex(x,y)
        dfdy = fun(x,y)/symmetric_derivativey(x,y)
        x = x - step_size*dfdx
        y = y - step_size*dfdy
        array_newton_x.append(x)
        array_newton_y.append(y)
        array_newton_z.append(eval(myfunction))
        if (abs(x-previous_x) < 1e-7) and (abs(x-previous_x) < 1e-7):
            return x,y
        elif a == (max_iter-1):
            return x,y

print("Function under consideration: " + myfunction)

#My own Newton-Raphson method
t = newton_raphson(initial_xvalue, initial_yvalue)
print("My Newton-Raphson: " + str(t))
print("Iterations needed: " + str(int(len(array_newton_x))-1))

def solver():
    #Using the built in equation solver in Sympy
    x = sp.symbols('x')
    y = sp.symbols('y')
    u = sp.solve(x**2 + y**2 - 1)
    #array_u = list()
    #array_u.append(u[0].values())
    print(u[0].values())
    print(u[1].values())
    #print("Sympy solve routine: " + str(u[0].values.evalf()) + " " + str(u[1].values.evalf()))

def plotting():
    #Plotting the function
    x = np.linspace(-1, 0, 400)
    y = np.linspace(-1, 0, 400)
    
    X, Y = np.meshgrid(x,y)
    Z = fun2(X,Y)
    z = np.linspace(-1,0,80)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.plot(array_newton_x, array_newton_y, z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z');

    ax.view_init(10, 0)
    fig
    
    #plt.plot(x, eval(myfunction), label=myfunction.replace('**', '^'))
    #plt.plot(array_newton_x, array_newton_y, 'ro', label='Newton-Raphson method, ' + str(int(len(array_newton_x))-1) + " iterations")
    #plt.legend()
    #plt.show()

plotting()
solver()

def builtin():
    #Using the built in newton method in Scipy
    z = initial_xvalue
    w = scp.newton(fun, 3, fun_der, tol=1e-7, maxiter=max_iter)
    print("Scipy newton solver " + str(w))