
##############################
# Binary - part II
##############################

from binary_I import *

##############################
# Activity 1 - Palindrome en binaire
##############################

## Question 1 ##

def is_palindrome_1(mylist):

    p = len(mylist)

    flag = True
    for i in range(p):
        if mylist[i] != mylist[p-1-i]:
            flag =  False

    return flag

# With optimization
def is_palindrome_1_bis(mylist):

    p = len(mylist)

    for i in range(p//2):
        if mylist[i] != mylist[p-1-i]:
            return False

    return True


def is_palindrome_2(mylist):
    mylist_inverse = list(reversed(mylist))
    return mylist == mylist_inverse


# Test 
print("--- Test: palindrome ---")
mylist = [1,0,1,0,0,1,0,1]
print(is_palindrome_1(mylist))
print(is_palindrome_1_bis(mylist))
print(is_palindrome_2(mylist))



## Question 2 ##


def find_binary_palindrome(N):
    num = 0
    for n in range(N):
        list_binary = integer_to_binary(n)
        if is_palindrome_1(list_binary) == True:
            num = num + 1
            print(num,":",n,"=",integer_to_binary(n))
    return

# Test
print("--- Binary palindromes ---")
find_binary_palindrome(1000)

# The 1000th palindrome in binary notation is:
#249903 = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]

## Question 3 ##

def find_decimal_palindrome(N):
    num = 0
    for n in range(N):
        list_decimal = integer_to_decimal(n)
        if is_palindrome_1(list_decimal) == True:
            num = num + 1
            print(num,":",n)
    return

# Test
print("--- Decimal palindromes ---")
find_decimal_palindrome(1000)

# The 1000th palindrome in decimal notation is:
# 90009

## Question 4 ##

def find_bi_palindrome(N):
    num = 0
    for n in range(N):
        list_binary = integer_to_binary(n)        
        list_decimal = integer_to_decimal(n)
        if is_palindrome_1(list_binary) == True and is_palindrome_1(list_decimal):
            num = num + 1
            print(num,":",n,"=",integer_to_binary(n))
    return

# Test
print("--- Bi-palindromes ---")
find_bi_palindrome(1000)

# The 20th bi-palindrome is: 
#  585585 = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1]




##############################
# Activity 2 - Opérations logiques
##############################

## Question 1 ##

def OReq(l1,l2):
    n = len(l1)    
    l = []
    for i in range(n):
        if l1[i]==1 or l2[i]==1:
            l = l + [1]
        else:
            l = l + [0]

    return l


def ANDeq(l1,l2):
    n = len(l1)
    l = []
    for i in range(n):
        if l1[i]==1 and l2[i]==1:
            l = l + [1]
        else:
            l = l + [0]
    return l


def NOT(l1):
    l = []
    for b in l1:
        if b==1:
            l = l + [0]
        else:
            l = l + [1]
    return l

# Test   
print("--- Logical operations (same length) ---")
l1 = [1,0,1,0,1,0,1]
l2 = [1,0,0,1,0,0,1]
print(l1)
print(l2)
print(OReq(l1,l2))
print(ANDeq(l1,l2))
print(NOT(l1))


## Question 2 ##


# Zero padding if necessary

def zero_padding(mylist,p):
    while len(mylist)< p:
        mylist = [0] + mylist

    return mylist

# Test 
print("--- Zero padding ---")
print(zero_padding([1,0,1,1],8))


## Question 3 ##

# Logical operations, with lists of different sizes

def OR(l1,l2):
    p = len(l1)
    q = len(l2)
    if p>q:
        ll2 = zero_padding(l2,p)   
        return OReq(l1,ll2)
    else:
        ll1 = zero_padding(l1,q)
        return OReq(ll1,l2)


def AND(l1,l2):
    p = len(l1)
    q = len(l2)
    if p>q:
        ll2 = zero_padding(l2,p)   
        return ANDeq(l1,ll2)
    else:
        ll1 = zero_padding(l1,q)
        return ANDeq(ll1,l2)


# Test   
print("--- Logical operation (general case) ---")
l1 = [1,0,1,0,1,0,1]
l2 = [1,0,0,1,0,]
print(l1)
print(l2)
print(OR(l1,l2))
print(AND(l1,l2))


##############################
# Activity 3 - Morgan law
##############################

## Question 1 ##

def every_binary_number_classical(p):
          
    list_all_p = []
    for n in range(2**p):
        list_all_p = list_all_p + [integer_to_binary(n)]
    return list_all_p


# Test 
print("--- All binary numbers ---")
print(every_binary_number_classical(3))


## Question 2 ##

def every_binary_number(p):
    if p == 0: 
      return []
    if p == 1: 
      return [[0],[1]]  

    list_all_p_1 = every_binary_number(p-1)

    list_all_p = [ [0] + l for l in list_all_p_1] + [ [1] + l for l in list_all_p_1]

    return list_all_p

# Test 
print("--- All binary numbers ---")
print(every_binary_number(3))



## Question 3 ##

# Lois de Morgan


def test_morgan_law(p):
    list_all = [zero_padding(l,p) for l in every_binary_number(p)]
    #list_all = every_binary_number(p)    
    for l1 in list_all:
        for l2 in list_all:
            not_l1_or_l2 = NOT(OR(l1,l2))
            not_l1_and_not_l2 = AND(NOT(l1),NOT(l2))
            if not_l1_or_l2 == not_l1_and_not_l2:
                print("It's true!")
                # pass
            else:
                print("It's false!",l1,l2)

    return

# Test
print("--- Test De Morgan law ---")
test_morgan_law(3)

