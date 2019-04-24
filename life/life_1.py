
##############################
# Game of life
##############################

##############################
# Activity 1 - Array
##############################


##################################################
## Question 1 ##

n, p = 5, 8;
array = [[0 for j in range(p)] for i in range(n)] 

# Blinker
array[2][2] = 1
array[2][3] = 1
array[2][4] = 1


##################################################
## Question 2 ##

def print_array(array):
    """ Print an array on the screen
    Input: a two dimensional arrayle
    Output: nothing (display on screen) """    

    for i in range(n):
        for j in range(p):
            print(array[i][j], end="")
        print()

    return


# Test 
print_array(array)

