
##############################
# If ... then ...
##############################

##############################
# Activity 4 - Triangles
##############################


# a,b,c = 3,4,5


##############################
## Question 1 ##

a = 4
b = 5
c = 8
print("Triangle",a,b,c)

# Do we have a <= b <= c?

if a <= b and b <= c:
    print("Lengths in the right order.")
else:
    print("Lengths in the wrong order.")


##############################
## Question 2 ##

# Can we construct a triangle from these three lengths?

if a+b >= c:
    print("Such a triangle exists.")
else:
    print("Such a triangle doesn't exist.")


##############################
## Question 3 ##

# Is the triangle recantgle?

if a**2 + b**2 == c**2:
    print("The triangle is rectangle.")
else:
    print("The triangle is not rectangle.")


##############################
## Question 3 ##

# Is the triangle equilateral?

if (a == b) and (b == c) and (a == c):
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")


##############################
## Question 4 ##

# Is the triangle isosceles?

if (a == b) or (b == c) or (a == c):
    print("The triangle is isosceles.")
else:
    print("The triangle is not isosceles.")


##############################
## Question 5 ##

# Are all the angles acute?

cosalpha = (-a**2 + b**2 + c**2)/(2*b*c)
cosbeta = (a**2 - b**2 + c**2)/(2*a*c)
cosgamma = (a**2 + b**2 - c**2)/(2*a*b)

if (cosalpha >= 0) and (cosbeta >= 0) and (cosgamma >= 0):
    print("All the angles are acute.")
else:
    print("Not all the angles are acute. (At least one of them is obtuse).")