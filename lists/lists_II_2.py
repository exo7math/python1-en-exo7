
##############################
# Lists II
##############################

from random import *


##############################
# Activity 2 - Reach a sum
##############################

##############################


from random import *
list_20 = [randint(1,99) for i in range(20)]
list_20 = [16, 2, 85, 27, 9, 45, 98, 73, 12, 26, 46, 25, 26, 49, 18, 99, 10, 86, 7, 42]
print(list_20)


list_200 = [randint(1,99) for i in range(200)]
print(list_200)

## Question 1 ##

##############################
# Find two elements in a row so that their sum is 100

def sum_twoinarow_100(mylist):
    n = len(mylist)
    for i in range(n-1):
        if mylist[i]+mylist[i+1] == 100:
            # print(i,i+1,mylist[i],mylist[i+1])
            return True
    return False


## Question 2 ##

##############################
# Find two distcint elements whose sum is 100
def sum_two_100(mylist):
    n = len(mylist)
    for i in range(n-1):
        for j in range(i+1,n):
            if mylist[i]+mylist[j] == 100:
                # print(i,j,mylist[i],mylist[j])
                return True
    return False


## Question 3 ##

##############################
# Sequence of terms whos sum is 100
def sum_seq_100(mylist):
    n = len(mylist)
    for i in range(n):
        mysum = 0
        j = i
        while mysum < 100 and j < n:
            mysum = mysum  + mylist[j]
            j = j + 1
        if mysum == 100:
            # print(i,j-1,mylist[i:j])
            return True
    return False

##############################
print("--- Sum: two in a row ---")
print(sum_twoinarow_100(list_20))
print(sum_twoinarow_100(list_200))

print("--- Sum: two anywhere ---")
print(sum_two_100(list_20))
print(sum_two_100(list_200))

print("--- Sum: sequence ---")
print(sum_seq_100(list_20))
print(sum_seq_100(list_200))

## Question 3 ##

##############################
# Proba: which length n give proba > 1/2 

def proba_1(n,N):
    nb = 0
    for k in range(N):
        mylist_n = mylist_n = [randint(1,99) for i in range(n)]
        found = sum_twoinarow_100(mylist_n)
        if found:
            nb += 1
    return nb/N


##############################
def proba_2(n,N):
    nb = 0
    for k in range(N):
        mylist_n = mylist_n = [randint(1,99) for i in range(n)]
        found = sum_two_100(mylist_n)
        if found:
            nb += 1
    return nb/N


##############################
def proba_3(n,N):
    nb = 0
    for k in range(N):
        mylist_n = mylist_n = [randint(1,99) for i in range(n)]
        found = sum_seq_100(mylist_n)
        if found:
            nb += 1
    return nb/N




print("--- Proba two in a row ---")
# Proba ~ 1/2 for length n ~ 67
print(proba_1(67,10000))

print("--- Proba two anywhere ---")
# Proba ~ 1/2 for length n ~ 12
print(proba_2(12,10000))

print("--- Proba sequence ---")
# Proba ~ 1/2 for length n ~ 42
print(proba_3(42,10000))