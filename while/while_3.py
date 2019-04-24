
##############################
# While - Boolean - Arithmetic
##############################


##############################
# Activity 3 - Divisor, prime numbers - Loop while (continued)
##############################


##############################
# Reminders from activity 2

def is_prime(n):
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

##############################
##############################


##############################
## Question 1 ##

def prime_number_after(n):
    """ Look for the first prime number after n """
    p = n
    while not is_prime(p):
        p = p + 1
    return p


# Test        
print("--- First prime number after an intger ---")
print(prime_number_after(60))
print(prime_number_after(100000))


##############################
## Question 2 ##

def twin_prime_after(n):
    """ Find twin primes after n """
    p = n
    q = p + 2
    while (not is_prime(p)) or (not is_prime(q)):
        p = p + 1
        q = p + 2
    return p,q


# Test    
print("--- First twin primes after an integer ---")
print(twin_prime_after(60))
print(twin_prime_after(100000))


##############################
## Question 3 ##

def germain_prime_after(n):
    """ Find two Germain primes after n """
    p = n
    q = 2*p + 1
    while (not is_prime(p)) or (not is_prime(q)):
        p = p + 1
        q = 2*p + 1
    return p,q


# Test    
print("--- First Germain primes after an integer ---")
print(germain_prime_after(60))
print(germain_prime_after(100000))


