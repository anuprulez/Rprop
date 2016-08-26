# Rpop Backpropogation algorithm used in Optimization (Machine Learning)

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:51:53 2015

@author: anupkumar
"""

# Rprop Gradient Descent #

from math import *
import numpy as np
import math
import matplotlib.pyplot as plt

def calculate_gradient_descent():
    u = 500  
    delta = 5
    etapos = 1
    etaneg = 1
    gradient_descent_prev = 0

    while return_gradient(u) != 0:
        if((gradient_descent_prev * return_gradient(u)) > 0):
            delta = etapos * delta
        elif((gradient_descent_prev * return_gradient(u)) < 0):
            delta = etaneg * delta

        if(return_gradient(u) < 0):
            u = u + delta
        elif(return_gradient(u) > 0):
            u = u - delta
            
        gradient_descent_prev = return_gradient(u)
        print return_gradient(u)
        cplot(u, return_function_value(u))


def return_function_value(u):
    f = (math.pow(u, 2)) - 100 * u - 100
    return f
    
    
def return_gradient(u):
     gradf = 2 * u - 100
     return gradf
    
    
def cplot(x, y): 
     plt.plot(x,y,'r.')  
     plot_function()
     plt.draw()
     plt.clf()  
    
    
def plot_function():  
    lx = []
    ly = []  
    input_values = np.arange(-1000,1000,0.1)
    for i in input_values:
        lx.append(i)
        ly.append(return_function_value(i))        
    plt.plot(lx,ly)
    plt.ion()
    plt.show()
    
    
calculate_gradient_descent()
