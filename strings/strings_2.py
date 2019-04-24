
##############################
# Strings - Text analysis 
##############################


##############################
# Activity 2 - Word games
##############################

## Question 1 ##

def hamming_distance(word1,word2):
    """ Compute the Hamming distance
    Input: two words of same length
    Output: the distance """

    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance = distance + 1

    return distance


# Test 
first_word = "SNAKE"
second_word = "STACK"
dist = hamming_distance(first_word,second_word)
print("The distance between",first_word,"and",second_word,"is",dist)

    
## Question 2 ##

def upsidedown(word):
    """ Reverse a word
    Input: a word (a string)
    Output: the reversed word  """

    revword = ""
    for charac in word:
        revword = charac + revword

    return revword


# Test 
word = "PYTHON"
revword = upsidedown(word)
print("The word",word,"becomes",revword,"!")



## Question 4 ##

def is_palindrome(word):
    """ Determined if a word is a palindrome
    Input: un word (a string)
    Output: true if it is a palindrome, false otherwise """

    revword = upsidedown(word)
    if word == revword:
        return True
    else: 
        return False


# Test 
word = "KAYAK"
print("Is the word",word,"a palindrome?",is_palindrome(word))




## Question 2 ##

def pig_latin(word):
    """ Transform a word to pig-latin
    Input: un word (une chaîne de charactères) 
    Output: le word transformed to pig-lation. """

    
    # Case: start with a vowels
    first_letter = word[0]
    if first_letter in ["A", "E", "I", "O", "U", "Y"]:  
        pig_latin = word + "WAY"

    # Case: start with consonants
    else:  
        i = 0
        while word[i] not in ["A", "E", "I", "O", "U", "Y"]:
            i = i + 1

        begin = word[0:i]
        end = word[i:]

        pig_latin = end + begin + "AY"

    return pig_latin


# Test 
word = "OMELET"
latin = pig_latin(word)
print("The pig-latin of",word,"is",latin,"!")
word = "STUPID"
latin = pig_latin(word)
print("The pig-latin of",word,"is",latin,"!")


