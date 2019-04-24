
##############################
# While - Boolean - Arithmetic
##############################


##############################
# Activity 2 - Divisor, prime number - Loop while
##############################


##############################
## Question 1 ##

def smallest_divisor(n):
    """ Find the smallest divisor of n """
    d = 2
    while n % d != 0:
        d = d + 1
    return d


# Test 
print("--- Smallest divisor ---")
print(smallest_divisor(7*13))


##############################
## Question 2 ##

def is_prime_1(n):
    """ Test if n is a prime number """

    d = 2    

    while n % d != 0:
        d = d + 1

    if d == n:
        return True    
    else:
        return False


# Test        
print("--- Is prime (1) ---")
print(is_prime_1(97))


##############################
## Question 3 ##

# Fermat numbers

def counter_example_fermat():
    for n in range(6): 
        fermat = 2**(2**n)+1
        print(n,fermat,is_prime_1(fermat))
    return  

# Test 
print("--- Test Fermat numbers conjecture ---")
counter_example_fermat()


##############################
## Question 4 ##

def is_prime_2(n):
    """ Test if n is a prime number """

    if n < 2:
        return False

    d = 2    

    while (n % d != 0) and (d**2 <= n):
        d = d + 1

    if d** 2 > n:
        return True    
    else:
        return False


# Test        
print("--- Is prime (2) ---")
print(is_prime_2(97))


##############################
## Question 4 ##


def is_prime_3(n):
    """ Test if n is a prime number """

    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    d = 3    
    while (n % d != 0) and (d**2 <= n):
        d = d + 2

    if d ** 2 > n:
        return True    
    else:
        return False


 # Test        
print("--- Is prime (3) ---")
print(is_prime_3(97))
       

##############################

## Question 5 ##

# Calculation of the execution times of the different functions is_prime()

import timeit
print(timeit.timeit("is_prime_1(97)", setup="from __main__ import is_prime_1", number=100000))
print(timeit.timeit("is_prime_2(97)", setup="from __main__ import is_prime_2", number=100000))
print(timeit.timeit("is_prime_3(97)", setup="from __main__ import is_prime_3", number=100000))


##############################
# We keep the best function!

def is_prime(n):
    return is_prime_3(n)