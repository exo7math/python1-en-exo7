
##############################
# Lists I
##############################


##############################
# Cours 1

mylist = [11,13,17,19]
mylist.append(23)
mylist.append(29)
print(mylist[5])
len(mylist)


##############################
# Activity 1 - Interst
##############################

## Question 1 ##

##############################
def simple_interests(S0,p,n):
    mylist = [S0]
    interest = S0 * p/100
    S = S0
    for i in range(n):
        S = S + interest
        mylist.append(S)
    return mylist


# Test
print("--- Simple interests ---")
list_simple_interests = simple_interests(1000,10,12)
print(list_simple_interests)
print(list_simple_interests[11])



## Question 2 ##

##############################
def compound_interests(S0,p,n):
    mylist = [S0]
    S = S0
    for i in range(n):
        interest = S * p/100
        S = S + interest
        mylist.append(S)
    return mylist


# Test
print("--- Compound interests ---")
list_compound_interests = compound_interests(1000,7,12)
print(list_compound_interests)
print(list_compound_interests[11])

