
##############################
# Strings - Text analysis 
##############################


##############################
# Activity 4 - Uppercase/lowercase
##############################


sentence = "Python is c@@l"
code = [ord(c) for c in sentence]
print(code)

## Question 1 ##

# With the machine
code = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 64, 64, 108]
sentence = ""
for c in code:
    sentence = sentence + chr(c)
print(sentence)




## Question 2 ##

for i in range(33,128):
    print(i," : ",chr(i))


## Question 3 ##

exp1 = 'chr(ord("a")-32)'
exp2 = 'chr(ord("B")+32)'

print(exp1," gives ",eval(exp1))
print(exp2," gives ",eval(exp2))


## Question 4 ##

def upper_letter(charac):
    """ Change a lower case to uppercase
    Input: a lowercase character among "a",...,"z"
    Output: the same letter but in uppercase """

    order = ord(charac)
    new_order = order - 32
    new_car = chr(new_order)

    return new_car


# Test 
print("The capital letter of 'a' is",upper_letter("a"))



## Question 5 ##

def uppercase(sentence):
    """ Transform a sentence to uppercase
    Input: a sentence (a string)
    Output: the same sentence in capital letters """
    
    new_sentence = ""
    for charac in sentence:
        order = ord(charac)
        if order >= 97 and order <= 122:
             # transformation to uppercase
            new_sentence = new_sentence + chr(order-32) 
        else: 
            # keep the character
            new_sentence = new_sentence + charac  

    return new_sentence


# Test 
sentence = "Hello world!"
print("The sentence",sentence,"becomes",uppercase(sentence))


# We will also need
def lowercase(sentence):
    """ Transform a sentence to lowercase
    Input: a sentence (a string)
    Output: the same sentence in lowercase """
    
    new_sentence = ""
    for charac in sentence:
        order = ord(charac)
        if order >= 65 and order <= 90:
             # transformation to lowercase
            new_sentence = new_sentence + chr(order+32) 
        else: 
            # keep the character
            new_sentence = new_sentence + charac  

    return new_sentence


## Question 6 ##

def format_full_name(somebody):
    """ Transform some name to the style "First LAST"
    Input: the first ans last name of someone (separated by a space)
    Output: the formated full name "First LAST" """
    
    # We split first and last name
    first = ""
    last = ""
    in_first = True     # We are in the first name
    for charac in somebody:
        if in_first:
            first = first + charac
        else:
            last = last + charac
        if charac == " ":
            in_first =  False    # End of teh first name

    # Format of the first name
    new_first = uppercase(first[0])+lowercase(first[1:len(first)])

    # Format of last name
    new_last = uppercase(last)
      
    return new_first+new_last


# Test 
somebody = "harry POTTER"
print(somebody,"devient",format_full_name(somebody))
somebody = "LORD Voldemort"
print(somebody,"devient",format_full_name(somebody))


