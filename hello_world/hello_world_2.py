
##############################
# Hello world!
##############################


##############################
# Activity 2 - Variables
##############################


##############################
# Lesson

# C1 - variables

a = 3  # One variable
b = 5  # Another variable

print("The sum is",a+b)   # Display the sum
print("The product",a*b)  # Display the product

c = b**a     # New variable...
print(c)     # ... that is displayed


# C2 - area of a triangle

base = 8
height = 3
area = base * height / 2
print(area)
# print(Area)  # !! Error !!


# C3 - Re-assignement

S = 1000
S = S + 100
S = S + 200
S = S - 50
print(S)


##############################
# Questions

# Q1

# Areas - Volumes

# Trapezoid: right namming
B, b, h = 7, 4, 3
area = (B + b) * h / 2
print("The area is",area)

# Box
L, l, h = 10,8,3
volume = L * l * h
print(volume)

# Disc
PI = 3.14
R = 10
area = PI * R**2
print(area)


# Q2 
# Put the lines back in order so that at the end x has the value 46.
x = 7
y = 2*x
y = y - 1
x = x + 3*y 
print(x)


# Q3
# Interest of 10%
S = 1000
S = S * 1.1
S = S * 1.1
S = S * 1.1


# Q4 

# Good way to exchange the values of a and b

# Wrong
a = 11
b = 9
a = b
b = a
print(a,b)

# Wrong
a = 11
b = 9
c = b
a = b
b = c
print(a,b)

# Wrong
a = 11
b = 9
c = a
a = c
c = b
b = c

print(a,b)

# Good
a = 11
b = 9
c = a
a = b
b = c
print(a,b)

