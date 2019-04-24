
##############################
# Lists II 
##############################


##############################
# Activity 1 - List comprehension
##############################


## Question 1 ##

##############################
def multiplication(list,k):
    return [k*x for x in list]


## Question 2 ##

##############################
def power(list,k):
    return [x**k for x in list]


## Question 3 ##

##############################
def addition(list1,list2):
    list_add = []
    for i in range(len(list1)):
        list_add.append(list1[i]+list2[i])
    return list_add


## Question 4 ##

##############################
def non_zero(list):
    return [x for x in list if x != 0]


## Question 5 ##

##############################
def even(list):
    return [x for x in list if x % 2 == 0]


# Test
print("--- Multiplication ---")
print(multiplication([1,2,3,4,5],2))
print("--- Power ---")
print(power([1,2,3,4,5],3))
print("--- Addition ---")
print(addition([1,2,3],[4,5,6]))
print("--- Without zeros ---")
print(non_zero([1,0,2,3,0,4,5,0]))
print("--- Pairs ---")
print(even([1,0,2,3,0,4,5,0]))


