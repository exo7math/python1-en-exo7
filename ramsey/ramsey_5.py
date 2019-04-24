
##############################
# Ramsey graphs and combinatorics
##############################


##############################
# Activity 5 - Proof n=6
##############################


from ramsey_1 import *
from ramsey_1 import has_3_friends_fix
from ramsey_1 import has_3_strangers_fix
from ramsey_3 import integer_to_binary
from ramsey_4 import subsets
from ramsey_4 import fix_subsets

##############################
##############################

# Subsets
n = 6
k = 3
SS_ENS_6_3 = fix_subsets(n,k)

## Question 1 ##

##################################################
def has_3(array):
    """Find if grpahe have 3 vertices friends/strangers"""
  
    n = len(array)

    #for sub in SS_ENS_6_3:  # For n=6, k=3
    for sub in fix_subsets(n,3):  # Fir any n 
        #print(sub)
        has_3_friends = has_3_friends_fix(array,*sub)
        has_3_strangers = has_3_strangers_fix(array,*sub)
        found = has_3_friends or has_3_strangers
        if found == True:
            break

    # Display
    # if found == True:
    #     print("OK for example:",sub)
    # else:
    #     print("Problem")
    # if found == False:
    #     print("Problem")
    #     print_graph(array)

    return found

# Test
# An example

if __name__ == '__main__':
    print("--- Test conjecture un seul graph ---")
    print("--- Example 1 ---")
    print(has_3(example_graph_1))
    print("--- Example 2 ---")
    print(has_3(example_graph_2))
    print("--- Example 3 ---")
    print(has_3(example_graph_3))
    print("--- Example 4 ---")
    print(has_3(example_graph_4))

## Question 2 ##

##################################################
##################################################
# Computation of all possibles graphs having n vertices
# There are 2^( (n-1)*n/2 )
def print_all_graphs(n):

    N = ((n-1) * n)//2
    print("Total number of graphs:",2**N)

    for p in range(2**N):
        # Binary conversion binary
        list_binary = integer_to_binary(p,N)

        print("p =",p,list_binary)

        graph = [[0 for j in range(n)] for i in range(n)] 

        for j in range(0,n):
            for i in range(j+1,n):
                b = list_binary.pop()
                graph[i][j] = b
                graph[j][i] = b

        print_graph(graph)

    return

 # Test
# n = 4
# print("--- Print all possible graphs ---")
# print("n = ",n)
# print_all_graphs(n)

## Question 3 ##

##################################################
##################################################
# Test all possible graph having n vertices
# Il y a 2^( (n-1)*n/2 )

def test_all_graphs(n):

    N = ((n-1) * n)//2
    print("Total number of graphs:",2**N)

    for p in range(2**N):
        # Binary conversion
        list_binary = integer_to_binary(p,N)

        # print("p =",p,list_binary)

        graph = [[0 for j in range(n)] for i in range(n)] 

        for j in range(0,n):
            for i in range(j+1,n):
                b = list_binary.pop()
                graph[i][j] = b
                graph[j][i] = b

        # print_graph(graph)
        test = has_3(graph)
        if test == False:
            print("Problem with",p)

    return

# Test
n = 6
print("\n\n--- Proof if Ramsey theorem for n = 6 ---")
print("n = ",n)
print("--- Looking for a graph that doesn't satisfy the proposition...")
test_all_graphs(n)
print("... end of computation ---")
print("If nothing has been printed, it's checked!")







