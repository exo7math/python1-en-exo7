
##############################
# Find and replace
##############################


##############################
# Activity 3 - Regex - Regular expressions 
##############################


## Question 1 ##


from re import *

def python_regex_find(string,exp):
    pattern = search(exp,string)
    if pattern:
        return pattern.group(), pattern.start(), pattern.end()
    else:
        return None

# Test
print("--- With regex search() ---")
string = "TO BE OR NOT TO BE"
exp = "N.T"
print(python_regex_find(string,exp))

exp = "B..O"
print(python_regex_find(string,exp))

exp = "[NM]O"
print(python_regex_find(string,exp))

exp = "[BC]..O[RS]"
print(python_regex_find(string,exp))


## Question 2 ##

# The wildcard "."

def regex_find_wildcard(string,exp):

    len_string = len(string)
    len_exp = len(exp)

    for i in range(len_string-len_exp+1):
        found = True
        for j in range(len_exp):
            if exp[j] != "." and string[i+j] != exp[j]:
                found = False
                break
        if found == True:
            return string[i:i+len_exp],i,i+len_exp
    return None

# Test
print("--- our regex wildcard ---")
string = "TO BE OR NOT TO BE"
exp = "N.T"
print(regex_find_wildcard(string,exp))


## Question 3 ##

# Choice "[AB]", or [ABC]

def all_choice(exp):
    list_exp = [""]
    mode_choice = False
    for c in exp:
        if c == "[": 
            mode_choice = True
            old_list_exp = list(list_exp)
            new_list_exp = []
        elif c == "]":
            mode_choice = False
            list_exp = new_list_exp
        else:
            if mode_choice == False:  # Normal mode
                list_exp = [ l + c for l in list_exp]
            else:  # Choice mode
                new_list_exp = new_list_exp + [ l + c for l in old_list_exp]      

    return list_exp

# Test
print("--- our regex choices ---")
exp = "[AB]X[CDE]Y"
print(all_choice(exp))


def regex_find_choice(string,exp):
    list_exp = all_choice(exp)
    for mon_exp in list_exp:
        result = python_regex_find(string,mon_exp)
        if result is not None:
            return result

    return None


# Test
print("--- regex choice ---")
string = "TO BE OR NOT TO BE"
exp = "N[OPQ]T"
print(regex_find_choice(string,exp))


## Question 4 ##

# Negation [^A] (or [^AB])

