

##############################
# Text viewer - Markdown
##############################


##############################
# Activity 3 - Justify text
##############################



################################################
## Question 1 ##

from random import randint

# list_lengths = [randint(5,15) for i in range(103)] 
# list_lengths = [14, 3, 16, 9, 2, 11, 13, 5, 4, 19, 16, 6, 17, 16, 15, 5, 14, 12, 17, 7]
list_lengths = [8, 11, 9, 14, 8, 8, 15, 10, 14, 11, 15, 15, 5, 12, 9, 9, 15, 10, 14, 5, 12, 8, 8, 13, 10, 11, 8, 13, 7, 5, 6, 11, 7, 7, 13, 6, 6, 9, 8, 12, 5, 8, 7, 6, 6, 15, 13, 11, 7, 12]

line_length = 100
space_length = 1

def justification_simple(list_len):
    """ Compute where to end the line for left alignment (without spaces)
    Input: a sequence of lengths (a list of integers)
    Output: the list of ranks where to cut the line """

    hyphen = [0]

    i = 1
    while i < len(list_len):
        mysum = list_len[i-1]

        while (i < len(list_len)) and (mysum <= line_length):
            mysum +=  list_len[i]
            i += 1

        if mysum > line_length:
            hyphen +=  [i-1]

    hyphen += [len(list_len)]

    return hyphen  


################################################
def print_justification_simple():
    """ Test: print justification simple """

    print("\n--- Justification without spaces ---")
    print("Length of words :",list_lengths)

    hyphen = justification_simple(list_lengths)   
    print("Justification:",hyphen)

    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        mysum = sum(line)
        print("\nLine",i,":",line,"\nIndex",hyphen[i],"to",hyphen[i+1]-1,"= list_len[",hyphen[i],":",hyphen[i+1],"]","\nSum =",mysum,"Remainder =",line_length-mysum,)

    return

# Test
print_justification_simple()



################################################
## Question 2 ##

def justification_spaces(list_len):
    """ Compute where to end the line for left alignment (wit spaces)
    Input: a sequence of lengths (a list of integers)
    Output: the list of ranks where to cut the line """

    hyphen = [0]

    i = 1

    while i < len(list_len):
        mysum = list_len[i-1]

        while (i < len(list_len)) and (mysum <= line_length):
            mysum +=  space_length + list_len[i]
            i += 1

        if mysum > line_length:
            hyphen +=  [i-1]            

    hyphen += [len(list_len)]

    return hyphen  



################################################
def print_justification_spaces():
    """ Test: print justifications with spaces """

    print("\n--- Justification with spaces ---")
    print("Length of words :",list_lengths)

    hyphen = justification_spaces(list_lengths) 
    print("Justification:",hyphen)

    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        nb_spaces = len(line)-1       
        mysum =  sum(line) + nb_spaces*space_length      
        print("\nLine",i,":",line,"\nIndex",hyphen[i],"to",hyphen[i+1]-1,"= list_len[",hyphen[i],":",hyphen[i+1],"]","\nSum with spaces =",mysum,"Remainder =",line_length-mysum,)

    return

# Test 
print_justification_spaces()



################################################
## Question 3 ##

def compute_space_lengths(list_len,hyphen):
    """ Compute the length of the spaces in order to justify the 'text'  (i.e. sum = 100)
    Input: a sequence of lengths (a list of integers) and the already computed justifications
    Output: the list of lengths for spaces for each line """   

    list_space_lengths = []
    
    for i in range(len(hyphen)-2):

        line = list_len[hyphen[i]:hyphen[i+1] ] 
        nb_spaces = len(line)-1
        mysum =  sum(line) + nb_spaces*space_length
        rest = line_length - mysum
        
        if nb_spaces > 0:
            new_space = space_length + rest / nb_spaces
        else:
            new_space = space_length

        list_space_lengths += [new_space]

    # Last line is not justified
    list_space_lengths += [space_length] 

    return list_space_lengths



################################################
def print_space_lengths():
    """ Test: print the lengths of the spaces to get justification """

    print("\n--- Justification with spaces ---")
    print("Length of words :",list_lengths)

    hyphen = justification_spaces(list_lengths) 
    print("Justification:",hyphen)

    list_space_lengths = compute_space_lengths(list_lengths,hyphen)
    print("Lengths of spaces for each line:",[float("{0:0.2f}".format(l)) for l in list_space_lengths])

    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        nb_spaces = len(line) - 1     
        mysum =  sum(line) + nb_spaces*list_space_lengths[i]   

        print("\nLine",i,":",line,"\nIndex",hyphen[i],"to",hyphen[i+1]-1,"= list_len[",hyphen[i],":",hyphen[i+1],"]","\nSum with spaces =",mysum,"Remainder =",line_length-mysum,)
        print("Lengths of the spaces for this line",list_space_lengths[i])

    return


# Test
print_space_lengths()




