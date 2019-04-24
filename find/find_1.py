
##############################
# Find and replace
##############################


##############################
# Activity 1 - Find
##############################

## Question 1 ##


def find_in(string,substring):
    return substring in string

# Test    
print("--- With 'in' ---")

string = "TO BE OR NOT TO BE"
substring = "NOT"
print(find_in(string,substring))


## Question 2 ##

def python_find(string,substring):
    position = string.find(substring)    
    return position

# Test 
print("--- With find() ---")

position = python_find(string,substring)
print(position)

position = python_find(string,"XYZ")
print(position)

## Question 3 ##

def find_index(string,substring):
    position = string.index(substring)    
    return position

# Test 
print("--- With index() ---")

position = find_index(string,substring)
print(position)

# position = find_index(string,"XYZ")
# print(position)


## Question 4 ##


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

# Test

print("--- Your own function ---")

position = myfind(string,substring)
print(position)

position = myfind(string,"XYZ")
print(position)

