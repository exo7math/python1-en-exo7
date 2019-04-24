
##############################
# Turtle
##############################


##############################
# Activity 3 - Graph of a function
##############################


from turtle import *
from math import *

speed("fastest")
width(2)
color('blue')
up()

for x in range(-200,200):
    if x == -199: down()
    # y = 1/ 100 * x ** 2   # Parabola
    y = 100*sin(1/20*x)     # Sine
    goto(x,y)


exitonclick()

