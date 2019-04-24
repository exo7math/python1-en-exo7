
##############################
# Functions
##############################

##############################
# Activity 4 - Functions
##############################

##################################################
## Question 1 ##

def reduction(age): 
    """ Return the percentage of discount with respect to the age """

    if age < 10:
        disc = 50 
    elif age <= 18:
        disc = 30
    elif age >= 60:
        disc = 20
    else:
        disc = 0

    return disc


# Test
print("--- Reduction ---")
my_age = 16 
print("I'm",my_age,"years old and my reduction is of",reduction(my_age),"%.")


##################################################


def amount(normal_rate,age):
    """ Compute the amount to pay with respect to normal rate and the age """

    reduc = reduction(age)
    rate = normal_rate * (100-reduc)/100

    return rate

# Test
print("--- Total amount to pay ---")
amout_family = amount(30,9) + 2*amount(20,16) + 2*amount(35,40)
print(amout_family)


##################################################
## Question 2 ##

def is_calculation_correct(a,b,answer):
    """ Test if the result of a*b is correct """

    if answer == a * b:
        return True
    else:
        return False


# Test
print("--- Test answer multiplication ---")
print(is_calculation_correct(6,7,42))

def test_multiplication(a,b,lang):
    """ Ask a multiplication in English or another language 
    and print if the answer is correct """

    # Sentence in English or French
    if lang == "english":
        question = "How much is the product a x b? "
        correct_answer = "Well done!"
        wrong_answer = "It's wrong!"

    if lang == "french":
        question = "Combien vaut le produit a x b ? "
        correct_answer = "Bravo !"
        wrong_answer = "Ce n'est pas cela !"

    # Interrogation
    print("--- Question ---")
    print("a =",a)
    print("b =",b)
    answer = int(input(question))

    if is_calculation_correct(a,b,answer):
        print(correct_answer)
    else:
        print(wrong_answer)

    return


# Test
print("--- Quiz multiplication ---")
test_multiplication(6,7,"french")
