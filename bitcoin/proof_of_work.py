
##############################
# Bitcoin
##############################


##############################
# Activity 1 - Proof of work
##############################

from time import *

# p = 101  # A small prime number
# p = 1097
# p = 10651
# p = 100109
# p = 1300573
p = 15486869 # A medium prime number
# p = 179426321  
# p = 2276856017 # A big prime number
# p = 32416187567


## Question 1 ##

def verification(x,y):
    xsquare = (x ** 2) % p
    if xsquare == y:
        return True
    else:
        return False


# Test
print("--- Vérification x^2 = y modulo p ---")      




start_chrono = time()

x = 6543210
# y = (x**2) % p; print(y)
y = 8371779  
print(verification(x,y))

end_chrono = time()
total_chrono = end_chrono - start_chrono
print("Time of computation (in seconds):",total_chrono)


## Question 2 ##

def square_root(y):
    for x in range(p):
        res = (x ** 2 - y) % p
        if res == 0:
            return x
    return None


# Test
print("--- Search for x st x^2 = y modulo p ---")  

start_chrono = time()

y = 8371779
x = square_root(y)
print(x, (x**2-y) % p)

end_chrono = time()
total_chrono = end_chrono - start_chrono
print("Time of computation (in seconds):",total_chrono)


## Question 3 ##

def approximate_square_root(y,margin):
    for x in range(p):
        res = (x ** 2 - y) % p
        if res <= margin:
            return x        
    return None


print("--- Recherche approchée de x tq x^2 = y modulo p ---")  

start_chrono = time()

y = 8371779
margin = 20
x = approximate_square_root(y,margin)
print("x =",x, "margin =",margin,"error =",(x**2-y) % p)

end_chrono = time()
total_chrono = end_chrono - start_chrono
print("Time of computation :",total_chrono)



## For intro of lesson ##

p = 15486869
y = 12345 ** 2
print(y % p)
x = square_root(y)
print(x, (x**2-y) % p)