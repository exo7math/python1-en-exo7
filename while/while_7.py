
##############################
# While - Boolean - Arithmetic
##############################

##############################
# Activity 7 - Square root
##############################

##################################################
## Question 1 ##


from math import *   

def square_root_1(n):
    """ Compute the integer square root of n
    Input: an integer
    Output: its integer square root """    

    real_root = sqrt(n)
    root = floor(real_root)

    return root


# Test 
print("--- Square root (1) ---")
print(square_root_1(10))
print(square_root_1(36))
print(square_root_1(56892))



##################################################
## Question 2 ##

def square_root_2(n):
    """ Compute the integer square root of n
    Input: an integer
    Output: its integer square root """  

    root = 0
    while root*root <= n:
        root = root + 1

    return root - 1


# Test 
print("--- Square root (2) ---")
print(square_root_2(10))
print(square_root_2(36))
print(square_root_2(56892))


##################################################
## Question 3 ##

def square_root_3(n):
    """ Compute the integer square root of n
    Input: an integer
    Output: its integer square root """    

    a = 1
    b = n
    while abs(a-b) > 1:
        a = (a+b)//2
        b = n//a
    return min(a,b)


# Tests
print("--- Square root (3) ---")
print(square_root_3(10))
print(square_root_3(36))
print(square_root_3(56892))


##################################################

def display_square_root_3(n):
    """ Display the steps of the computation of the square root by the last methd 
    Input: an integer
    Output: its integer square root
    Action: display steps """

    a = 1
    b = n
    i = 0
    print("--- Square root of",n,"---")
    print("i =",i," ;  a = ",a," ;  b = ",b)

    while abs(a-b) > 1:
        a = (a+b)//2
        b = n//a
        i = i +1
        print("i =",i," ;  a = ",a," ;  b = ",b)
    print("Integer square root of",n,"is",min(a,b))

    return min(a,b)


# Tests
display_square_root_3(10)
display_square_root_3(1664)


##################################################
# Test 

# print("--- Test ---")
# for i in range(1,1000000):
#     # print(i)
#     if square_root_1(i) != square_root_3(i):
#         print('Warning for',i)   
# print('Fin test')


##################################################
## Variant Question 3 ##

def square_root_4(n):
    """ Compute the integer square root of n
    Input: an integer
    Output: its integer square root """     


    un = n
    un1 = (un + n//un) // 2

    while un1 < un:
        un = un1
        un1 = (un + n//un) // 2

    return un

# Test 
print("--- Square root (4) ---")
print(square_root_4(10))
print(square_root_4(36))
print(square_root_4(56892))

