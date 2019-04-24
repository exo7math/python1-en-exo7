
##############################
# If ... then ...
##############################

##############################
# Fctivity 2 - Turtle
##############################

from turtle import *

width(5)
color('blue')

mot = "FflFlFrFlFFlfFF"

for c in mot:

    if c == "F":
        forward(100)

    if c == "f":
        up()
        forward(100)
        down()   

    if c == "l":
        left(90)

    if c == "r":
        right(90) 

exitonclick()
