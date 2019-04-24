
##############################
# Turtle
##############################

##############################
# Activity 4 - Several turtles - The pursuit
##############################

# Preparation

from turtle import *

turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()

turtle1.speed("fastest")
turtle2.speed("fastest")
turtle3.speed("fastest")
turtle4.speed("fastest")

turtle1.color('red')
turtle2.color('blue')
turtle3.color('orange')
turtle4.color('green')

# turtle1.width(5)
# turtle2.width(5)
# turtle3.width(5)
# turtle4.width(5)

turtle1.up()
turtle1.goto(-200,-200)
turtle1.down()

turtle2.up()
turtle2.goto(200,-200)
turtle2.down()

turtle3.up()
turtle3.goto(200,200)
turtle3.down()

turtle4.up()
turtle4.goto(-200,200)
turtle4.down()

print(turtle1.position())
print(turtle1.towards(0,0))


# Main loop

for i in range(40):

    position1 = turtle1.position()
    position2 = turtle2.position()
    position3 = turtle3.position()
    position4 = turtle4.position()

    turtle1.goto(position2)  # Go where is the next turtle
    turtle1.goto(position1)  # and go back to its position

    turtle2.goto(position3)
    turtle2.goto(position2)

    turtle3.goto(position4)
    turtle3.goto(position3)

    turtle4.goto(position1)
    turtle4.goto(position4)

    angle1 = turtle1.towards(position2)  # Memorize the angle
    turtle1.setheading(angle1)   # Set the direction with this angle

    angle2 = turtle2.towards(position3)
    turtle2.setheading(angle2)

    angle3 = turtle3.towards(position4)
    turtle3.setheading(angle3)

    angle4 = turtle4.towards(position1)
    turtle4.setheading(angle4)

    turtle1.forward(10)    # Move
    turtle2.forward(10)
    turtle3.forward(10)
    turtle4.forward(10)

exitonclick()



