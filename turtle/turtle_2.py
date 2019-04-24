
##############################
# Turtle
##############################

##############################
# Activity 2 - Loop "for"
##############################

##############################
# Question 1

from turtle import *

# A pentagon
width(5)
color('blue')

for i in range(5):
    forward(100)
    left(72)


##############################
# Question 2

# An other pentagon
color('red')

longueur = 200
angle = 72
for i in range(5):
    forward(longueur)
    left(angle)


##############################
# Question 3

# A dodecagon (12 edges)

color("purple")
n = 12
angle = 360/n
for i in range(n):
    forward(100)
    left(angle)


##############################
# Question 4

# A spiral

color("green")
length = 10
for i in range(25):
    forward(length)
    left(40)
    length = length + 10

exitonclick()


