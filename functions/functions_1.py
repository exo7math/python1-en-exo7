
##############################
# Functions
##############################

##############################
# Activity 1 - Introduction to functions
##############################

##################################################
## Question 1 ##

# Function without parameter, without output

def print_table_of_7():
    """ Display the table of 7 """

    print("--- Table of 7 ---")
    for i in range(1,11):
        print(i,"x 7 =",str(i*7))

    return


# Test
print_table_of_7()


##################################################


def print_hello():
    """ Say hello """

    prenom = input("What's your name? ")
    print("Hello",prenom)

    return

# Test
print_hello()


##################################################
## Question 2 ##

# Function with parameter, sans sortie

def print_a_table(n):
    """ Print the table of n """

    print("--- Table of",n,"---")
    for i in range(1,11):
        print(i,"x",n,"=",str(i*n))

    return


# Test
print_a_table(5)


##################################################

def say_greeting(sentence):
    """ Say hello, hi, goodbye... """

    name = input("What's your name? ")
    print(sentence,name)

    return


# Test
say_greeting("Goodbye")
  


##################################################
## Question 3 ##

# Function without parameter, with output

def ask_name():
    """ Ask and return the first and last names """
    
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    full_name = first_name + " " + last_name.upper()

    return full_name


# Test
identity = ask_name()
print("Identity:",identity)


