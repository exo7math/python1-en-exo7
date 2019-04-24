
##############################
# Functions
##############################



##############################
# Lesson 1
##############################

##################################################

def say_hello():
    print("Hello world!")
    return

# Call
say_hello()
say_hello()

##################################################
def print_squares():
    for i in range(20):
        print(i**2)
    return

# Call
print_squares()


##############################
# Lesson 2
##############################

##################################################
def display_month(number):
    if number == 1:
        print("We are in January.")
    if number == 2:
        print("We are in February.")
    if number == 3:
        print("We are in March.")
    # etc.
    return

# Call
display_month(2)


##################################################
def compute_cube(a):
    cube = a * a * a  # or a**3
    return cube

# Call
x = 3
y = 4
z = compute_cube(x) + compute_cube(y)
print(z)


##############################
# Lesson 2
##############################

##################################################
def sum_product(a,b):
    """ Computes the sum and product of two numbers. """
    s = a + b
    p = a * b
    return s, p

# Call
mysum, myprod = sum_product(6,7)
print(mysum,myprod)

##############################
# Lesson - Local variable
##############################

x = 7

def add_one(x):
    x = x + 1
    return x

def double(x):
    x = 2*x
    return x

print(x)
print(add_one(x))
print(double(x))
print(x)




