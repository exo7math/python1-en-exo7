
##############################
# While - Boolean - Arithmetic
##############################


##############################
# Activity 1 - Divisibility, quotient, remainder
##############################


##############################
## Question 1 ##

def quotient_remainder(a,b):
    """ Displays the quotient and remainder and checks
    the validity of the Euclidean division """

    q = a // b
    r = a % b
    print("Division of a =",a,"by b =",b)
    print("The quotient is q =",q)
    print("The remainder is r =",r)

    if (r >=0) and (r < b):
        check_remainder = True
    else:
        check_remainder = False
    print("Check remainder: 0 <= r < b ?",check_remainder)

    if a == b*q +r:
        check_equal = True
    else:
        check_equal = False
    print("Check a = bq + r ?",check_equal)

    return q,r


# Test
print("--- Quotient and remainder ---")
quotient_remainder(100,7)


##############################
## Question 2 ##

def is_even(n):
    """ Tests if the integer n is even or not (returns true or false) """
    remainder = n % 2
    if remainder == 0:
        return True
    else:
        return False


def is_even_bis(n):
    """ Tests if the integer n is even or not (returns true or false) """
    unit = n % 10
    if (unit==0) or (unit==2) or (unit==4) or (unit==6) or (unit==8):
        return True
    else:
        return False


# With two lines!
def is_even_ter(n):
    return (n % 2) == 0


# Test
print("--- Even/odd  ---")
print(is_even(1023))


##############################
## Question 3 ##

def is_divisible(a,b):
    """ Test if a is divisible per b """    
    if a % b == 0:
        return True
    else:
        return False


# Test
print("--- Divisibility  ---")
print(is_divisible(125,5))

