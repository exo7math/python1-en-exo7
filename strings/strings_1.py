
##############################
# Strings - Text analysis 
##############################


##############################
# Activity 1 - Plurals
##############################

## Question 1 ##

word = "cat"
plural = word + "s"
print("Singular:",word)
print("Plural:",plural)


## Question 2 ##

# word = "cat"
word = "bus"

last_letter = word[len(word)-1]

if last_letter == "s":
    plural = word + "es"
else:
    plural = word + "s"

print("Singular:",word)
print("Plural:",plural)


## Question 3 ##

# word = "cat"
# word = "bus"
word = "city" 

last_letter = word[len(word)-1]

if last_letter == "s":
    plural = word
elif last_letter == "y":
    begin_word = word[0:len(word)-1]
    plural = begin_word + "ies"
else:
    plural = word + 's'

print("Singular:",word)
print("Plural:",plural)



## Question 4 ##


# It's better with a function!

def plural(word):
    """ Return the plural of the given word.
    Input: a word
    Output: the plural of the word (except exceptions) """

    last_letter = word[len(word)-1]

    if last_letter == "s":
        plural = word
    
    elif last_letter == "y":
        begin_word = word[0:len(word)-1]
        plural = begin_word + "ies"

    else:
        plural = word + 's'


    return plural


# Test 
#word = input("Give me a noun: ")
#plural = plural(word)
#print("The plural is:",plural)


## Question 5 ##

def conjugation(verb):
    """ Conjugate a verb to present continuous tense.
    Input: a verb
    Output: print its conjugation """

    
    print("I'm " + verb + "ing")
    print("You're " + verb + "ing")  
    print("He/she is " + verb + "ing")
    print("We are " + verb + "ing")
    print("You are " + verb + "ing")
    print("They are " + verb + "ing")


    return


# Test 
verb = "sing"
#verb = input("Give me a verb: ")
conjugation(verb)





     
