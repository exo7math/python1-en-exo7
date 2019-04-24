
##############################
# Lists I
##############################

##############################
##############################
# Lesson 2

mylist = []
mylist = mylist + ["One"]
mylist = ["Two"] + mylist
mylist[1:5]


##############################
# Activity 2 - Manipulation of lists
##############################

## Question 1 ##

##############################
def rotate(thelist):
    n = len(thelist)
    new_list = [thelist[n-1]] + thelist[0:n-1]
    return new_list

# Test
print("--- Rotation ---")
print(rotate([1,2,3,4]))


## Question 2 ##

##############################
def inverse(thelist):
    new_list = []
    for element in thelist:
        new_list = [element] + new_list
    return new_list

# Test
print("--- Inverse ---")
print(inverse([1,2,3,4]))


## Question 3 ##

##############################
def delete_rank(thelist,rang):
    n = len(thelist)
    new_list = thelist[0:rang]+thelist[rang+1:n]
    return new_list

# Test
print("--- Delete item at a given rank ---")
print(delete_rank([8,7,6,5,4],2))


## Question 4 ##

##############################
def delete_element(thelist,element):
    new_list = []
    for x in thelist:
        if x != element:
            new_list = new_list + [x]
    return new_list

# Test
print("--- Delete an element ---")
print(delete_element([8,7,4,6,5,4],4))



##############################
##############################
# Lesson 3 - Manipulation : conclusion

# reverse, reversed, [::-1]

print("--- Lesson ---")
thelist = [1,2,3,4]
print(thelist[::-1])
thelist.reverse()
print(thelist)

print(list(reversed(thelist)))



# Othe idea with remove()


print("--- remove() ---")
thelist = [2,5,3,8,5]
print(thelist)
thelist.remove(5)
print(thelist)
thelist.remove(5)
print(thelist)


# See also "del"