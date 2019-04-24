
##############################
# Ramsey graphs and combinatorics
##############################


##############################
# Activity 1 - Définition et amis/étrangers
##############################

## Question 1 ##

##################################################

# Example 1
n = 3
example_graph_1 = [[0 for j in range(n)] for i in range(n)] 
example_graph_1[0][1] = 1; example_graph_1[1][0] = 1
example_graph_1[0][2] = 1; example_graph_1[2][0] = 1

# Example 2
n = 4

example_graph_2 = [[0 for j in range(n)] for i in range(n)] 

example_graph_2[0][2] = 1; example_graph_2[2][0] = 1 
example_graph_2[0][3] = 1; example_graph_2[3][0] = 1
example_graph_2[1][2] = 1; example_graph_2[2][1] = 1


# Example 3
n = 5

example_graph_3 = [[0 for j in range(n)] for i in range(n)] 

example_graph_3[0][2] = 1; example_graph_3[2][0] = 1 
example_graph_3[0][3] = 1; example_graph_3[3][0] = 1
example_graph_3[1][2] = 1; example_graph_3[2][1] = 1
example_graph_3[1][4] = 1; example_graph_3[4][1] = 1
example_graph_3[3][4] = 1; example_graph_3[4][3] = 1 

# Example 4
n = 6

example_graph_4 = [[0 for j in range(n)] for i in range(n)] 

example_graph_4[3][2] = 1; example_graph_4[2][3] = 1; 
example_graph_4[1][2] = 1; example_graph_4[2][1] = 1
example_graph_4[3][4] = 1; example_graph_4[4][3] = 1
example_graph_4[4][1] = 1; example_graph_4[1][4] = 1
example_graph_4[0][2] = 1; example_graph_4[2][0] = 1
example_graph_4[5][0] = 1; example_graph_4[0][5] = 1
example_graph_4[5][1] = 1; example_graph_4[1][5] = 1
example_graph_4[0][3] = 1; example_graph_4[3][0] = 1


# Example for the lesson 
n = 4

example_graph_lesson_1 = [[0 for j in range(n)] for i in range(n)] 

example_graph_lesson_1[0][2] = 1; example_graph_lesson_1[2][0] = 1 
example_graph_lesson_1[1][3] = 1; example_graph_lesson_1[3][1] = 1

## Question 2 ##

##################################################
def print_graph(array):
    """
    Print an array on the screen
    Input: un array
    Output: nothing (print on screen)
    """    
    
    n = len(array)

    for j in range(n):
        for i in range(n):
            print(array[i][j], end="")
        print()

    return

# Test 
if __name__ == '__main__':
    print("--- Array of the graph ---")
    print("--- Example 1 ---")
    print_graph(example_graph_1)
    print("--- Example 2 ---")
    print_graph(example_graph_2)
    print("--- Example 3 ---")
    print_graph(example_graph_3)
    print("--- Example 4 ---")
    print_graph(example_graph_4)

    print("--- Lesson 1 ---")
    print_graph(example_graph_lesson_1)    

##################################################
##################################################
# Test if a graph contains 3 friends/3strangers


##################################################
def has_3_friends_fix(array,i,j,k):
    """ Test if the vertices i, j, k are linked has friends"""
    if array[i][j] == 1 and array[i][k] == 1 and array[j][k] == 1:
        return True
    else:
        return False

##################################################
def has_3_strangers_fix(array,i,j,k):
    """Test if the vertices i, j, k  are strangers together"""
    if array[i][j] == 0 and array[i][k] == 0 and array[j][k] == 0:
        return True
    else:
        return False        

# Test
if __name__ == '__main__':
    print("--- Has 3 friends? Has 3 strangers? ---")
    print(has_3_friends_fix(example_graph_4,1,3,4))
    print(has_3_strangers_fix(example_graph_4,1,3,4))

 