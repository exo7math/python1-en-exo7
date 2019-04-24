
##############################
# Functions
##############################


##############################
# Activity 3 - Turtle
##############################

from turtle import *
width(5)    # Width of the pencil

##############################
## Question 1 ##

def triangle():
    color('red')
    forward(200)
    left(120)
    forward(200)
    left(120)
    forward(200)
    return


# Test
# triangle()
# exitonclick()

##############################
## Question 2 ##

def square():
    color('green')
    for i in range(4):
        forward(200)
        left(90)
    return


# Test
# square()
# exitonclick()


##############################
## Question 3 ##

def hexagon(length):
    color('blue')
    for i in range(6):
        forward(length)
        left(60)
    return


# Test
# hexagon(100)
# exitonclick()


##############################
## Question 4 ##

def polygon(n,length):
    color('purple')
    angle = 360/n
    for i in range(n):
        forward(length)
        left(angle)
    return


# Test
# polygon(10,70)
# exitonclick()

# Test all
up()
goto(-450,0)
down()
triangle()
up()
goto(-200,0)
setheading(0)
down()
square()
up()
goto(100,0)
setheading(0)
down()
hexagon(100)
up()
goto(320,0)
setheading(0)
down()
polygon(8,70)
up()
exitonclick()