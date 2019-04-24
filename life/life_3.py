
##############################
# Game of life
##############################


##############################
# From Activity 1
##############################

from life_1 import *

n, p = 5, 8;
array = [[0 for j in range(p)] for i in range(n)] 

# Blinker
array[2][2] = 1
array[2][3] = 1
array[2][4] = 1


##############################
# Activity 3 - Evolution
##############################


##################################################
## Question 1 ##

def number_neighbors(i,j,array):
    """ Compute the nb of living neighbors of the box (i,j)
    Input: a box position in a array of cells
    Output: the nb of neighbor cells """ 

    nb = 0
    # Neighbor top left
    if (i>0) and (j>0) and (array[i-1][j-1] != 0):
        nb += 1
    # Neighbor just above
    if (i>0) and (array[i-1][j] != 0):
        nb += 1
    # Neighbor top right
    if (i>0) and (j<p-1) and (array[i-1][j+1] != 0):
        nb += 1
    # Neighbor left
    if (j>0) and (array[i][j-1] != 0):
        nb += 1
    # Neighbor rigth
    if (j<p-1) and (array[i][j+1] != 0):
        nb += 1
   # Neighbor left below
    if (i<n-1) and (j>0) and (array[i+1][j-1] != 0):
        nb += 1
    # Neighbor just below
    if (i<n-1) and (array[i+1][j] != 0):
        nb += 1
    # Neighbor right below
    if (i<n-1) and (j<p-1) and (array[i+1][j+1] != 0):
        nb += 1

    return nb

# Test
print("--- Number of neighbors ---")
print(number_neighbors(1,1,array))
print(number_neighbors(2,1,array))
print(number_neighbors(3,1,array))
print(number_neighbors(2,0,array))
print(number_neighbors(2,2,array))
print(number_neighbors(3,3,array))

##################################################

def print_neighbors(array):
    """ Print the nb of living neighbors
    Input: an array
    Output: nothin (print on the screen) """    

    for i in range(n):
        for j in range(p):
            print(number_neighbors(i,j,array), end='')
        print()

    return


# Test
print("--- Initial configuration ---")
print_array(array)
print("--- Number of neighbors ---")
print_neighbors(array)


##################################################
## Question 2 ##

def evolution(array):
    """ Caompute the evolution to the next day
    Input: an array
    Output: an array """    

    new_array = [[0 for j in range(p)] for i in range(n)]

    for j in range(p):
        for i in range(n):
            # Cell alive or not?
            if array[i][j] != 0:
                cellule_alive = True
            else:
                cellule_alive = False

            # Nombres de neighbors
            nb_neighbors = number_neighbors(i,j,array)

            # Règle du jeu de la vie
            if cellule_alive == True and (nb_neighbors == 2 or nb_neighbors == 3):
                new_array[i][j] = 1
            if cellule_alive == False and nb_neighbors == 3:
                new_array[i][j] = 1          

    return new_array


# Test
print("--- Initial configuration ---")
print_array(array)
print("--- Number of neighbors ---")
print_neighbors(array)
print("--- After evolution ---")
array = evolution(array)
print_array(array)



