
##############################
# While - Boolean - Arithmetic
##############################


##############################
# Activity 4 - Goldbach conjecture(s)
##############################

from math import *

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
##############################


##############################
## Question 1 ##

# Goldbach's (good) conjecture (1742): 
# any even integer greater than 3 is the sum of two prime numbers

def number_solutions_goldbach(n):
    """ Compute the number of decomposition n = p + q with
    n even ; p, q primes and q >= p """

    # If n odd, it's over
    if n % 2 == 1:
        print("Attention! Integer not even.")
        return None

    nb_sol = 0

    for p in range(2,n//2+1):
        q = n - p
        if (q>=p) and (is_prime(p)) and (is_prime(q)):
            print("n =",n,"sum of p =",p,", q = ",q)
            nb_sol = nb_sol + 1

    return nb_sol


# Test    
print("--- Goldbach's conjecture  ---")
print(number_solutions_goldbach(100))


def test_goldbach_conjecture(nmax):
    """ Checks the validity of the Goldbach conjecture
    for even integers from 4 to nmax """

    print("Start of the test")
    for n in range(4,nmax,2):
        if number_solutions_goldbach(n) == 0:
            print("Problem with n = ",n)
    print("End of the test")
    return


# Test    
print("--- Conjecture de Goldbach ---")
test_goldbach_conjecture(10000)


##############################
## Question 2 ##

# Goldbach 1752 : 
# every odd integer can be written as
# n = p + 2k^2
# with p prime and k integer (k maybe 0)

def is_decomposition_goldbach(n):
    """ Test if the odd n can be written n = p + 2k^2
    with p prime and k integer """

    maxk = ceil(sqrt(n/2))+1
    for k in range(maxk):
        p = n - 2 * k**2
        if is_prime(p):
            # print(n,p,k,n-p-2*k**2)
            return True    
    return False


def counter_example_goldbach(nmax):
    """ Cherche un contre-exemple à la seconde conjecture de Goldbach """
    print("--- Start of the search ---")
    for m in range(1,nmax):
        n = 2 * m + 1
        if is_decomposition_goldbach(n) == False:
            print("Counter-example :",n)

    print("--- End of the search ---")
    return

# Test 
print("--- Test wrong Goldbach's conjecture ---")
print("Avec 5777 : ",is_decomposition_goldbach(5777))
counter_example_goldbach(10000)



