
##############################
# Lists II - Magic squares
##############################

from random import *


##############################
# From activity 3 

def print_array(array):
    """
    Print a square on screen
    Input: an array of size n x n
    Output: nothing (display on terminal)
    """    
    
    n = len(array)

    for i in range(n):
        for j in range(n):
            print('{:>3d}'.format(array[i][j])," ", end="")
        print()

    return

##############################
def sum_diagonal(array):
    n = len(array)
    somme = 0
    for i in range(n):
        somme = somme + array[i][i]
    return somme


##############################
def sum_antidiagonal(array):
    n = len(array)
    somme = 0
    for i in range(n):
        somme = somme + array[n-1-i][i]
    return somme


##############################
# Activity 4 - Magic squares
##############################

## Question 1 ##

##############################

print("--- Magic square ---")
# square = [ [1,2,3], [4,5,6], [7,8,9] ]
square_3x3 = [ [4,9,2], [3,5,7], [8,1,6] ]
square_4x4 = [ [1,14,15,4], [7,9,6,12], [10,8,11,5], [16,3,2,13] ]
print("--- Square 3x3 ---")
print_array(square_3x3)
print("--- Square 4x4 ---")
print_array(square_4x4)


## Question 2 ##

##############################
def is_magic_square(square):
    n = len(square)
    total = n * (n**2 + 1) // 2

    if sum_diagonal(square) != total:
        return False

    if sum_antidiagonal(square) != total:
        return False            

    for row in square:
        if sum(row) != total:
            return False

    for j in range(n):
        S = 0
        for i in range(n):
            S = S + square[i][j]
        if S != total:
            return False

    return True

print("--- Check magic square ---")
print(is_magic_square(square_3x3))
print(is_magic_square(square_4x4))


## Question 3 ##

##############################
def random_square(n):

    integers = list(range(1,n**2+1))
    shuffle(integers)
    square = [ integers[i*n:(i+1)*n] for i in range(n) ]
    return square

print("--- Square aléatoire ---")
square = random_square(4)
print_array(square)
print(is_magic_square(square))


## Question 4 ##

##############################
def addition_square(square,k):

    n = len(square)
    new_square = [[0 for j in range(n)] for i in range(n)]   

    for i in range(n):
        for j in range(n):
            new_square[i][j] = square[i][j] + k

    return new_square



## Question 4 ##

##############################
def multiplication_square(square,k):

    n = len(square)
    new_square = [[0 for j in range(n)] for i in range(n)]   

    for i in range(n):
        for j in range(n):
            new_square[i][j] = square[i][j] * k

    return new_square

# Test 
print("--- Addition, multiplication of magic square ---")
# square = [ [1,2,3], [4,5,6], [7,8,9] ]
square = [ [4,9,2], [3,5,7], [8,1,6] ]
sum_square = addition_square(square,-1)
product_square = multiplication_square(square,9)
print_array(square)
print_array(sum_square)
print_array(product_square)


## Question 5 ##

##############################
def homothety_square(square,k):

    n = len(square)
    new_square = [[0 for j in range(k*n)] for i in range(k*n)]   

    for i in range(k*n):
        for j in range(k*n):
            new_square[i][j] = square[i//k][j//k]

    return new_square

# Test 
print("--- Homothety magic square ---")
# square = [ [1,2,3], [4,5,6], [7,8,9] ]
# square = [ [4,9,2], [3,5,7], [8,1,6] ]
# big_square = homothety_square(square,3)
# print_array(big_square)

big_square = homothety_square(square_3x3,3)
print_array(big_square)

big_square = homothety_square(square_4x4,2)
print_array(big_square)


## Question 6 ##

##############################
def addition_block_square(big_square,small_square):

    N = len(big_square)
    n = len(small_square)
    # m = N//n

    new_square = [[0 for j in range(N)] for i in range(N)]   

    for i in range(N):
        for j in range(N):
            new_square[i][j] = big_square[i][j] + small_square[i%n][j%n]

    return new_square

    # Test 
print("--- Addition of blocks - Magic square ---")
small_square = [ [1,2], [3,4] ]
square = [ [1,2,3], [4,5,6], [7,8,9] ]
big_square = homothety_square(square,2)
new_big_square = addition_block_square(big_square,small_square)
print_array(small_square)
print("---")
print_array(big_square)
print("---")
print_array(new_big_square)


## Question 7 ##

##############################
def product_squares(square1,square2):
    n = len(square1)
    # m = len(square2)

    square3a = addition_square(square2,-1)
    # print("---")
    # print_array(square3a)
    square3b = homothety_square(square3a,n)
    # print("---")
    # print_array(square3b)
    square3c = multiplication_square(square3b,n**2)
    # print("---")
    # print_array(square3c)    
    square3d = addition_block_square(square3c,square1)
    # print("---")
    # print_array(square3d)

    return square3d


#### Test ####
square1 = [ [4,9,2], [3,5,7], [8,1,6] ]
square2 = [ [4,14,15,1], [9,7,6,12], [5,11,10,8], [16,2,3,13] ]
square3 = product_squares(square1,square2)
print("--- Product of squares ---")
print_array(square1)
print("---")
print_array(square2)
print("---")
print_array(square3)
print(is_magic_square(square3))


#### Product doesn't commute (a*b is not b*a) ####
square4 = product_squares(square2,square1)
print("--- Product of squares ---")
print_array(square1)
print("---")
print_array(square2)
print("---")
print_array(square4)
print(is_magic_square(square4))


#### Square of size 36 x 36 ####
square5 = product_squares(square1,square4)
# print_array(square5)
print(is_magic_square(square5))