
##############################
# Functions
##############################

##############################
# Activity 2 - Functions
##############################

##################################################
## Question 1 ##

# Function with parameter, with output

def trinomial_1(x):
    """ Compute 3x^2-7x+4 """

    result = 3*x**2 - 7*x + 4

    return result


# Test
print("--- Trinomial ---")
for i in range(10):
    print("The value at x =",i,"is",trinomial_1(i))


##################################################


def trinomial_2(a,b,c,x):
    """ Compute ax^2+bx+c """

    result = a*x**2 + b*x + c

    return result


# Test
a = 2 ; b = -1 ; c = 0
print("Trinomial for a,b,c =",a,b,c)
for i in range(10):
    print("The value at x =",i,"is",trinomial_2(a,b,c,i))



##################################################
## Question 2 ##

# Function with parameter, with sortie

def conversion_dollars_to_euros(amount):
    """ Convert an amount given in dollars to euros """

    amount_euro = 0.89 * amount

    return amount_euro


# Test
print("--- Currency ---")
x = 20
print(x,"dollars is", conversion_dollars_to_euros(x),"euros")


##################################################


def conversion_dollars(amount,currency):
    """ Convert an amount given in dollars to another currency """

    if currency == "euro":
        rate = 0.89
    if currency == "pound":
        rate = 0.77
    if currency == "yen":
        rate = 110
       
    amount_currency = amount * rate
 
    return amount_currency


# Test
x = 100
for mycurrency in ["yen","euro","pound"]:
    print(x,"dollars equal", conversion_dollars(x,mycurrency),mycurrency)



##################################################
## Question 3 ##

from math import *

# Compute several volumes

def volume_cube(a):         
    return a**3

def volume_ball(r):         
    return 4/3 * pi * r**3

def volume_cylinder(r,h):
    return pi * r**2 * h

def volume_box(a,b,c):
    return a * b * c

# Test
print("--- Volumes ---")
print(volume_cube(3))
print(volume_ball(3))
print(volume_cylinder(2,5))
print(volume_box(3,4,5))


##################################################
## Question 4 ##

def perimeter_area_rectangle(a,b):
    """ Compute the perimeter and the area 
    of a rectangle of side a and b """

    p = 2*a+2*b
    A = a * b

    return p, A

def perimeter_area_disc(r):
    """ Compute perimeter and area 
    of a disc of radius r """

    p = 2 * pi * r
    A = pi * r**2

    return p, A

print("--- Perimeters et areas ---")
print(perimeter_area_rectangle(4,5))
print(perimeter_area_disc(3))


# Experimental research: comparison perimeter/area of a disc

for R in range(0,30):
    perimeter, area = perimeter_area_disc(R/10)
    print(R/10, perimeter - area)

# Experimental conclusion:
#   for 0 < r < 2, the perimeter is strictly greater than its area
#   pour r = 2, the perimeter is equal to area,
#   pour r > 2, the perimeter is strictly lower than the area 
