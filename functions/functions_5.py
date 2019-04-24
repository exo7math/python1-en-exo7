
##############################
# Functions
##############################


##############################
# Activity 5 - Egalité expérimentale
##############################

from math import *

##################################################
## Question 1 ##

def absolute_value(x):
    if x >= 0:
        return x
    else:
        return -x


##################################################
def root_of_square(x):
    return sqrt(x**2)
    

##################################################
def experimental_equality_1(f,g):
    """ Teste si deux Functions sont expérimentalement égales """
    for i in range(-100,101):
        if f(i) != g(i):
            return False
    return True

# Test
print("--- Egalité experimentale, une variable ---")
# print(experimental_equality_1(absolute_value,absolute_value_moins))  # True
print(experimental_equality_1(absolute_value,root_of_square))       # True


##################################################
## Question 2 ##

def F1(a,b):
    return (a+b)**2


##################################################
def F2(a,b):
    return a**2 + 2*a*b + b**2


##################################################
def F3(a,b):
    return (a-b)**3


##################################################
def F4(a,b):
    return a**3 - 3*a**2*b  - 3*a * b**2 + b**3


##################################################
def F5(a,b):
    return a**3 - 3*a**2*b  + 3*a * b**2 - b**3


################################################
def experimental_equality_2(F,G):
    """ Test if two functions of two variables are experimentally equal """

    for i in range(-100,101):
        for j in range(-100,101):
            if F(i,j) != G(i,j):
                # print(i,j,F(i,j),G(i,j))
                return False
    return True

# Test
print("--- Experimental equality, two variables ---")
print(experimental_equality_2(F1,F2))   # True
print(experimental_equality_2(F3,F4))   # False
print(experimental_equality_2(F3,F5))   # True


################################################
## Question 3 ##

def sincos(x):
    return sin(x)**2 + cos(x)**2


################################################
def un(x):
    return 1


##################################################

precision = 0.00001   # = 10**-5  

def experimental_equality_3(f,g):
    """ Test if two functions are experimentally equalt
    with an error margin """   

    for i in range(-100,101):
        if abs(f(i) - g(i))> precision :
            return False
    return True

# Test
print("--- Approximate experimental equality ---")
print(experimental_equality_1(sincos,un))  # False !! But yould be True !
print(sin(3)**2+cos(3)**2)         #  Explenation: Python does not exactly return 1 
print(experimental_equality_3(sincos,un))  # True !


# Test with with other equalities, examples :
# sin(2x) = 2 sin(x)cos(x)
# cos(pi/2 - x) = sin(x)


################################################
# A wrong equality but experimentally true

def g1(x):
    return sin(pi*x)

################################################

def g2(x):
    return 0

print("--- A wrong equality but experimentally true ---")
print(experimental_equality_3(g1,g2))  # True (we always have equality for all integer i)
print(g1(1/2))  # however g1(0.5) is not zero, hence the equality is not true in general
