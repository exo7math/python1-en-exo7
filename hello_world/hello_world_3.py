
##############################
# Hello world!
##############################


##############################
# Activity 3 - Use functions
##############################


##############################
# Cours

# C1 - functions

print("Hi there.")

x = float("+1.234567")
print(x)


# C2 - math module

from math import *

x = sqrt(2)
print(x)
print(x**2)

# C3 - sine and cosine

angle = pi/2
print(angle)
print(sin(angle))


# C4 - decimal number to integer

x = 3.6
print(round(x))
print(floor(x))
print(ceil(x))


##############################
# Questions

# Q1
# gcd
print(gcd(13*121,13*122))

a = 101*103
b = 102*103
print(a,b)
lcm = a * b // gcd(a,b)
print(lcm)


# Q2
# Absolute value
x = 3.85
print(abs(x**2-15))
print(round(2*x))
print(floor(3*x))
print(ceil(4*x))


# Q3
# Angle
angle = pi/7
x = cos(angle)**2 + sin(angle)**2
print(x)

