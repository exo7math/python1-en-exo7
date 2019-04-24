
##############################
# While - Boolean - Arithmetic
##############################


##############################
# Activity 5 - Integers ayant 4 ou 8 divisors
##############################


# Conjecture: between 1 and N, there are more integers with (exactly)
# 4 divisors than integers with 8 divisors

##############################
## Question 1 ##

def number_of_divisors_1(n):
    """ Number of divisors of n (1 and n are included) """
    nb = 0
    for d in range(1,n+1):
        if n % d == 0:
            nb = nb + 1
    return nb


def number_of_divisors_2(n):
    """ Number of divisors of n (1 and n are included) """    
    nb = 2  # we already count 1 and n
    for d in range(2,n//2+1):
        if n % d == 0:
            nb = nb + 1
    return nb


# We choose the best method
def number_of_divisors(n):
    return number_of_divisors_2(n)


# Test 
print("--- Number of divisors ---")
print(number_of_divisors(100))


##############################

## Question 2 ##

def four_and_eight_divisors(Nmin,Nmax):
    nb_four = 0 
    nb_eight = 0
    for n in range(Nmin,Nmax):
        nb = number_of_divisors(n)
        if nb == 4:
            nb_four = nb_four + 1
        if nb == 8:
            nb_eight = nb_eight + 1
    return nb_four, nb_eight


# Test 
print("--- Number having 4, then 8 divisors ---")
print(four_and_eight_divisors(1,100))


##############################

## Question 3 ##

# Search of a couter-example to the conjecture
# N must be large enough, for instance
# between 1 and N = 250000 there are more integers
# having 8 divisors than 4 divisors


# By slices of of 50 000 (computations are long!)

# print(four_and_eight_divisors(1,50000))
# print(four_and_eight_divisors(50000,100000))
# print(four_and_eight_divisors(100000,150000))
# print(four_and_eight_divisors(150000,200000))
# print(four_and_eight_divisors(200000,250000))

# Slice 1: 12073, 10957
# Slice 2: 11254, 11224
# Slice 3: 10995, 11229
# Slice 4: 10838, 11218
# Slice 5: 10690, 11260

# 4 divisors 12073+11254+10995+10838+10690   = 55850
# 8 divisors 10957+11224+11229+11218+11260   = 55888

