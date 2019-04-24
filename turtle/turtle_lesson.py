
##############################
# Turtle
##############################

##############################
# Lesson - Turtle
##############################

from turtle import *

forward(100)   # Move forward
left(90)       # Turn 90 degrees left
forward(50)
width(5)       # Width of the pencil
forward(100)
color('red')
right(90)
forward(200)

exitonclick()

#################
# Lesson - Several turtles
#################

tortue1 = Turtle()   # With capital 'T'!
tortue2 = Turtle()

tortue1.color('red')
tortue2.color('blue')

tortue1.forward(100)
tortue2.left(90)
tortue2.forward(100)