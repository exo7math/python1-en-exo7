
##############################
# Find and replace
##############################

##############################
##############################
# From activity  1

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
# Activity 2 - Replace 
##############################

string = "TO BE OR NOT TO BE"
substring = "OR"
new_substring = "AND"


## Question 1 ##

print("--- With replace() ---")
new_string = string.replace(substring,new_substring)
print(new_string)


## Question 2 ##

# your own function replace using myfind()

def myreplace(string,substring,new_substring):
    pos = myfind(string,substring)

    if pos is not None:  # If found (short version "if not pos:")
        endpos = pos + len(substring)
        string = string[:pos]+new_substring+string[endpos:]

    return string

print("--- Replace: our function ---")
new_string = myreplace(string,substring,new_substring)
print(new_string)


## Question 3 ##

#
# replace_all() : replace all occurences


def replace_all(string,substring,new_substring):

    pos = myfind(string,substring)
        
    while pos is not None:  # as long as not found
        endpos = pos+len(substring)
        string = string[:pos]+new_substring+string[endpos:]
        pos = myfind(string,substring)

    return string

# Attention: this function is to simple because A -> AB will loop forever

print("--- Remplace all: our function ---")
string = "TO BE OR NOT TO BE"
substring = "BE"
new_substring = "HAVE"
new_string = replace_all(string,substring,new_substring)
print(new_string)


