
##############################
# Lists II
##############################

##############################
# Activity 3 - Array
##############################


## Question 1 ##

##############################
def sum_diagonal(array):
    n = len(array)
    S = 0
    for i in range(n):
        S = S + array[i][i]
    return S


## Question 2 ##

##############################
def sum_antidiagonal(array):
    n = len(array)
    S = 0
    for i in range(n):
        S = S + array[n-1-i][i]
    return S


## Question 3 ##

##############################
def sum_all(array):
    n = len(array)    
    S = 0
    for i in range(n):
        for j in range(n):
            S = S + array[i][i]
    return S


## Question 4 ##

##############################
def print_array(array):
    """
    Print a square on screen
    Input: an array of size n x n
    Output: nothing (display on terminal)
    """       
   
    n = len(array)
    for i in range(n):
        for j in range(n):
            print('{:>3d}'.format(array[i][j]),end="")
        print()
    return




##############################
array = [ [1,2,3], [4,5,6], [7,8,9] ]

print("--- Sum diagonale---")
print(sum_diagonal(array))

print("--- Sum anti-diagonal ---")
print(sum_antidiagonal(array))

print("--- Sum all ---")
print(sum_all(array))

print("--- Display ---")
print_array(array)

