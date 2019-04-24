
##############################
# Lists I
##############################


##############################
# Activity 4 - Arithmetic
##############################

## Question 1 ##

##############################
def prime_factors(n):
    thelist = []
    d = 2
    while d <= n:
        if n%d == 0:
            thelist = thelist + [d]
            n = n // d
        else:
            d = d + 1
    # if len(thelist)==0:   # Case of a prime number
    #     thelist = [n]
    return thelist


# Test
print("--- Prime factors ---")
n = 2*2*2*3*7*7*11
print(n)
print(prime_factors(2*2*2*3*7*7*11))


## Question 2 ##

##############################
def list_primes(n):
    thelist = list(range(2,n))
    for d in range(2,n):
        for k in thelist:
            if k%d == 0 and k != d:
                thelist.remove(k)
    return thelist

print("--- List of primes numbers ---")
print(list_primes(100))

