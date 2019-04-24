
##############################
# Lists I
##############################


##############################
# Activity 5 - Balistics
##############################

import matplotlib.pyplot as plt
from math import *

def parabolic_shot(x,v,alpha):
    g = 9.81
    alpha = 2*pi/360*alpha  # angle in radians
    y = -1/2 * g / (v * cos(alpha))**2 * x**2  +  tan(alpha) * x
    return y

def list_abscissa(xmax,n):
    list_x = []
    for i in range(n+1):
        x = i * xmax/n  
        list_x.append(x)
    return list_x    

def list_trajectory(xmax,n,v,alpha):
    list_y = []
    for i in range(n+1):
        x = i * xmax/n  
        y = parabolic_shot(x,v,alpha)
        list_y.append(y)
    return list_y

list_x = list_abscissa(270,100)
tir30 = list_trajectory(270,100,50,30)
tir45 = list_trajectory(270,100,50,45)
tir60 = list_trajectory(270,100,50,60)
plt.plot(list_x,tir30,color="blue")
plt.plot(list_x,tir45,color="red")
plt.plot(list_x,tir60,color="green")
plt.grid()
plt.show()
