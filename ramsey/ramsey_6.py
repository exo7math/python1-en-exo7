
##############################
# Ramsey graphs and combinatorics
##############################


##############################
# Activity 6 - To go further
##############################


from ramsey_1 import *
from ramsey_1 import has_3_friends_fix
from ramsey_1 import has_3_strangers_fix
from ramsey_3 import integer_to_binary
from ramsey_4 import subsets
from ramsey_4 import fix_subsets

##############################
##############################



## Question 1 ##

# Subsets
n = 6
k = 3
SS_ENS_3 = fix_subsets(n,k)



##################################################
def has_3(graph):
    """Find if graph has 3 vertices friends/strangers"""
  
    n = len(graph)

    for sub in SS_ENS_3:  
        has_3_friends = has_3_friends_fix(graph,*sub)
        has_3_strangers = has_3_strangers_fix(graph,*sub)
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


# Test all possibles graphs having n vertices
# Il y a 2^( (n-1)*n/2 )

def test_all_graphs(n):

    N = ((n-1) * n)//2
    print("Total number of graphs:",2**N)

    for p in range( ((2**N) // 2)):
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
            print("Problem with graph p =",p)

    return

# Test
n = 6
print("\n\n--- Proof if Ramsey theorem for n = 6 ---")
print("n = ",n)
print("--- Looking for a graph that doesn't satisfy the proposition...")
test_all_graphs(n)
print("... end of computation ---")
print("If nothing has been printed, it's checked!")


# n = 6 : 0.5 seconds
# n = 7 : 20 seconds
# n = 8 : 2500 seconds = 40 min (extrapolation simpling of 10^-2 %)
# n = 9 : 800 000 seconds = 9 jours (extrapolation from simplang of 10^-4 %)


## Question 2 ##

##################################################
##################################################

# Subsets
n = 7
SS_ENS_3 = fix_subsets(n,3)
SS_ENS_4 = fix_subsets(n,4)

##################################################
def has_4_friends_fix(graph,i,j,k,l):
    """Test if vertices i, j, k,l are all linked"""
    if graph[i][j] == 1 and graph[i][k] == 1 and graph[i][l] == 1 and graph[j][k] == 1 and graph[j][l] == 1 and graph[k][l] == 1:
        return True
    else:
        return False

# Test of all possible graphs having n vertices
# to see if there 4 friends or 3 strangers


def has_3_4(graph):
    """Test if 3 or 4 vertices are links"""

    n = len(graph)

    # Look for 3 strangers
    for sub in SS_ENS_3:  
        has_3_strangers = has_3_strangers_fix(graph,*sub)
        if has_3_strangers == True:
            break

    # If not 3 strangers, look for 4 friends
    if has_3_strangers == False:
        for sub in SS_ENS_4:  
            found_4_friends = has_4_friends_fix(graph,*sub)
            if found_4_friends == True:
                break
    else: 
        found_4_friends = True # Doesn't matter, since 3 strangers

    found = has_3_strangers or found_4_friends


    return found



def ramsey_4_3(n):

    N = ((n-1) * n)//2
    print("Total number of graphs:",2**N)

    # for p in range(  ((2**N)) // 100000 ):
    for p in range( 1000000 ):    
        # Binary conversion
        list_binary = integer_to_binary(p,N)

        # print("p =",p,list_binary)

        graph = [[0 for j in range(n)] for i in range(n)] 

        for j in range(0,n):
            for i in range(j+1,n):
                b = list_binary.pop()
                graph[i][j] = b
                graph[j][i] = b


        test = has_3_4(graph)
        if test == False:
            print("Problem with the graph p =",p)

    return

# Test
print("\n\n--- Proof of Ramsey theorem with 4 friends or 3 strangers, n =",n,"---")
print("n = ",n)
print("--- Looking for a graph that doesn't satisfy the proposition...")
ramsey_4_3(n)
print("... end of computation ---")
print("If nothing has been printed, it's checked!")


# n = 7, easy and many counter-examples
# n = 8 counter examples for instance p=111121101
# n = 9 is True! But should have 18 days of computations