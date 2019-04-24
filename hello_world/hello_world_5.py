
##############################
# Hello world!
##############################


##############################
# Activity 5 - Loop "for" (continued)
##############################

# Questions

# Q1
# Sum of the squares
n = 20
mysum = 0
for i in range(n+1):
    mysum = mysum + i**2
print(mysum)


# Q2
# Products
n = 19
myproduct = 1
for i in range(1,n+1,2):
    myproduct = myproduct * i
print(myproduct)


# Q3
# Multiplication tables
for a in range(11):
    for b in range(11):
        print(a,"x",b,"=",a*b)