# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a  
    while k < 3: 
        k =k + 1 
        a = a * (-1) * x **2/((2*k)*(2*k+1))
        S = S + a
        return S

a = 1.57
b = 4.71
x = np.arange(a,b,0.01)
y = mans_sinuss(x)
plt.plot(x,y)
plt.grid()
plt.show()
