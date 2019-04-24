
##############################
# Ramsey graphs and combinatorics
##############################


##############################
# Activity 4 - Subsets
##############################

from ramsey_3 import integer_to_binary


##############################
##############################



## Question 1 ##


# Genration of all subsets

##################################################
def subsets(n):
    """Find all subsets of a set  [0,1,2,...n-1] having n elements """

    all_subsets = []

    for p in range(2**n):

        # Binary conversion
        list_binary = integer_to_binary(p,n)
        #print(list_binary)

        sub = []
        for j in range(n):
            # if list_binary[n-j-1] == 1:  
            if list_binary[j] == 1:                
                sub = sub + [j]

        all_subsets = all_subsets + [sub]

    return all_subsets

# Test 
if __name__ == '__main__':
    print("--- Subsets ---")
    n = 3
    SS_ENS = subsets(n) 
    print("For n = ",n)
    print("Number of subsets = ",len(SS_ENS))
    print(SS_ENS)


## Question 2 ##

##################################################
def fix_subsets(n,k):
    all_fix_subsets = []
    for sub in subsets(n):
        if len(sub) == k:
            all_fix_subsets = all_fix_subsets + [sub]
    return all_fix_subsets

# Test (suite)
if __name__ == '__main__':
    print("--- Sous-ensembles à 3 éléments ---")

    n = 6
    k = 3
    SS_ENS_3 = fix_subsets(n,k)
    print("For n = ",n," k = ",k)
    print("Number of subsets having",k,"elements = ",len(SS_ENS_3))
    print(SS_ENS_3)






