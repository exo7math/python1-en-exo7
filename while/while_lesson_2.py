
##############################
# While II
##############################

##############################
# Lesson 2 - break
##############################

##############################
# Example 1

# Countdown
n = 10
while True:     # Infinite loop
    print(n)
    n = n - 1
    if n < 0:
        break   # Immediate stop

# Better (with a flag)
n = 10
finished = False
while not finished:
    print(n)
    n = n - 1   
    if n < 0:
        finished = True

# Even better (after reformulation)
n = 10
while n >= 0:
    print(n)
    n = n - 1

##############################
# Example 2

# Integer square root
n = 777
for i in range(100):
    if i**2 > n:
        break
print(i-1)


# Better
n = 777
i = 0 
while i**2 <= n:
    i = i + 1
print(i-1) 


##############################
# Example 3

from math import *

# Square root of the elements of a list
mylist = [3,7,0,10,-1,12]
for element in mylist:
    if element < 0:
        break
    print(sqrt(element))


# Better with try/except
mylist = [3,7,0,10,-1,12]
for element in mylist:
    try: 
        print(sqrt(element))
    except:
        print("Warning, I don't know have to compute the square root of",element)







  
