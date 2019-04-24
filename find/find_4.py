
##############################
# Find and replace
##############################


##############################
# From activity 1
##############################

def myfind(string,substring):
    len_string = len(string)
    len_substring = len(substring)
    for i in range(len_string-len_substring+1):
        found = True
        for j in range(len_substring):
            if string[i+j] != substring[j]:
                found = False
                break
        if found == True:
            return i
    return None

##############################
# From activity 2 - replace
##############################

def myreplace(string,substring,new_substring):
    pos = myfind(string,substring)

    if pos is not None:  # If found (short version "if not pos:")
        endpos = pos + len(substring)
        string = string[:pos]+new_substring+string[endpos:]

    return string


##############################
# Activity 4 - Itérations
##############################


## Question 1 ##

 # Test

print("--- One iteration ---")

print("-- Ex 1 --")
sentence = "01001110"
pattern = "01"
new_pattern = "10"
new_sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
print(new_sentence)

print("-- Ex 2 --")
sentence = "01001110"
pattern = "0011"
new_pattern = "1100"
new_sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
print(new_sentence)

print("-- Ex 3 --")
sentence = "01001110"
pattern = "0011"
new_pattern = "111000"
new_sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
print(new_sentence)

print("-- Ex 4 --")
sentence = "0001"
pattern = "01"
new_pattern = "1100"
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)



## Question 2 ##

# Global constant for the maximum number of iterations
MAX_ITER = 1000


def iterations(sentence,pattern,new_pattern):
    i = 0
    while i <= MAX_ITER:
        new_sentence = myreplace(sentence,pattern,new_pattern)
        if sentence == new_sentence:
            return i, sentence
        else:
            sentence = new_sentence
            i = i+1
    return None


print("--- Iterations ---")
print("-- Ex 1 --")
sentence = "000011011"
pattern = "0011"
new_pattern = "1100"
result = iterations(sentence,pattern,new_pattern)
print(result)

sentence = "000011011"
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)
sentence = myreplace(sentence,pattern,new_pattern)
print(sentence)

print("-- Ex 2 --")

sentence = "000011011"
pattern = "001"
new_pattern = "11000"
result = iterations(sentence,pattern,new_pattern)
print(result)

## For Question 3 ##


## binary with zero padding ##

def integer_to_binary(n,p):
    string_b = bin(n)  # Binary notation as a string
    string_b = string_b[2:]   # We remove the prefix

    # Padding with zero if necessary
    nb_zeros = p - len(string_b)
    for i in range(nb_zeros):
        string_b = "0" + string_b

    return string_b

# Test
print("--- Binary notation with zero-padding ---")
print(integer_to_binary(33,8))

## Question 3 ##

def max_iterations(p,pattern,new_pattern):

    maxi_iter = 0
    sentence_maxi_iter = ""
    new_sentence_maxi_iter = ""

    for n in range(2**p):
        sentence = integer_to_binary(n,p)
        result = iterations(sentence,pattern,new_pattern)
        #print(result)
        if result is None:
            return None, sentence
        else:
            nb_iter = result[0]
            if nb_iter > maxi_iter:
                maxi_iter = nb_iter 
                sentence_maxi_iter = sentence  
                new_sentence_maxi_iter = result[1]
    return maxi_iter, sentence_maxi_iter, new_sentence_maxi_iter

print("--- Maximal iterations ---")

# Exemple
pattern = "01"
new_pattern = "100"
print(max_iterations(4,pattern,new_pattern))


## Question 4 ##


# Lineair
pattern = "0011"
new_pattern = "110"
print("- Lineaire -")
print(max_iterations(10,pattern,new_pattern))

# Quadratic
pattern = "01"
new_pattern = "10"
print("- Quadratic -")
print(max_iterations(10,pattern,new_pattern))

# Exponential
pattern = "01"
new_pattern = "110"
print("- Exponential -")
print(max_iterations(10,pattern,new_pattern))

# Ne termine pas
pattern = "01"
new_pattern = "1100"
print("- No ending -")
print(max_iterations(4,pattern,new_pattern))



