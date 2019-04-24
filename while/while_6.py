
##############################
# While - Boolean - Arithmetic
##############################

##############################
# Activity 6 - Wrong conjecture: 1211111... is never prime
##############################


##############################
# From activity 2

def is_prime(n):
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

       
##############################
## Question 1 ##

def one_two_one(k):
    """ Compute an integer 121111... """
    u = 12
    for i in range(k):
        u = 10*u + 1
    return u


# Test 
print("--- 121111.... ---")
u = one_two_one(10)
print(u) 



##############################
## Question 2 ##

# Conjecture 1211111... is never prime

def test_prime_one_two_one(kmax):
    """ Test if 121111... is prime or not """
    for k in range(kmax):
        uk = one_two_one(k)
        print(k,"  ",uk,"is prime ?",is_prime(uk))      
    return


# Test 
print("--- Test conjecture 121111.... never prime ---")
test_prime_one_two_one(21)

# Will not yields to a counter-example
# Because computations are too long


##############################
## Question 3 ##

def is_almost_prime(n,r):
    """ Test if n has no divisor <= r """

    if n < 2: return False
    if n == 2: return True    
    if n % 2 == 0: return False

    d = 3    
    while (n % d != 0) and (d ** 2 <= n) and (d <= r):
        d = d + 2

    if (d ** 2 > n) or (d > r):
        return True    
    else:
        return False

# Test 
print("--- Test almost prime ---")
print(is_almost_prime(101,13))

##############################

## Question 4 ##

def test_almost_one_two_one(kmax):
    """ Test if 121111... is almost prime """

    n = 12
    for k in range(kmax):
        if is_almost_prime(n,1000000):
            print(k,"  ",n,'is almost prime')
        n = 10*n + 1
    return

# Test 
print("--- Test conj 121111.... never almost prime ---")
test_almost_one_two_one(151)