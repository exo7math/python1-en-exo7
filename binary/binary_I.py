
##############################
# Binary - part I
##############################

##############################
# Activity 1 - From decimal notation to integer
##############################

## Question 1 ##

def decimal_to_integer_1(list_decimal):
    number = 0
    p = len(list_decimal)
    for i in range(p):
        d = list_decimal[p-1-i]
        number = number + d*10**i

    return number

## Question 1bis ##


def decimal_to_integer_2(list_decimal):
    number = 0
    i = 0
    for d in reversed(list_decimal):
        number = number + d*10**i
        i = i + 1

    return number

# Test
print("--- Decimal notation to integer ---")
mylist = [1,2,3,4]
print(decimal_to_integer_1(mylist))
print(decimal_to_integer_2(mylist))


##############################
# Activity 2 - Binary notation to  integer
##############################



## Question 1 ##

def binary_to_integer_1(list_binary):
    number = 0
    p = len(list_binary)
    for i in range(p):
        if list_binary[p-1-i] == 1:
            number = number + 2**i

    return number

## Question 1bis ##

def binary_to_integer_2(list_binary):
    number = 0
    i = 0
    for b in reversed(list_binary):
        if b == 1:
            number = number + 2**i
        i = i + 1

    return number



## Question 2 ##

def binary_to_integer_bis(list_binary):
    number = 0
    for b in list_binary:
        if b == 0:
            number = number*2
        else:
            number = number*2 + 1

    return number



# Test
print("--- Binary notation to integer ---")
mylist = [1,1,0,1,1,0,0,1]
print(binary_to_integer_1(mylist))
print(binary_to_integer_2(mylist))
print(binary_to_integer_bis(mylist))



##############################
# Activity 3 - Decimal notation
##############################


def integer_to_decimal(n):
    if n==0: return [0]
    list_decimal = []
    while n != 0:
        list_decimal = [n%10] + list_decimal
        n = n//10
    return list_decimal


# Test
print("--- Integer to decimal notation ---")
n = 1234
mylist = integer_to_decimal(n)
integer = decimal_to_integer_1(mylist)
print(n)
print(mylist)
print(integer)



##############################
# Activity 4 - Binary notation
##############################


def integer_to_binary(n):
    if n==0: return [0]
    list_binary = []
    while n != 0:
        list_binary = [n%2] + list_binary
        n = n//2
    return list_binary

# Test
print("--- Integer to binary notation ---")
n = 1234
mylist = integer_to_binary(n)
integer = binary_to_integer_1(mylist)
print(n)
print(mylist)
print(integer)

