
##############################
# Hyphenation of a list - Justify text
##############################

from random import randint
list_lengths_words = [randint(1,20) for i in range(50)] 
#list_len_words = [14, 3, 16, 9, 2, 11, 13, 5, 4, 19, 16, 6, 17, 16, 15, 5, 14, 12, 17, 7]


line_length = 100
space_length = 1


################################################
def hyphenation_simple(list_len_words,list_len_line):
    hyphen = [0]
    i = 1

    while i < len(list_len_words):
        mysum = list_len_words[i-1]

        while (i < len(list_len_words)) and (mysum <= list_len_line):
            mysum = mysum + list_len_words[i]
            i = i + 1

        hyphen = hyphen + [i-1]

    hyphen = hyphen + [len(list_len_words)+1]

    return hyphen  


################################################
def print_hyphenation_simple(list_len_words,hyphen):
    print("\n--- Hyphenation sans spaces ---")
    print("list_lengths des words",list_len_words)
    print("hyphen",hyphen)
    for i in range(len(hyphen)-1):
        line = list_len_words[hyphen[i]:hyphen[i+1]]
        mysum = sum(line)
        print(i,"---",line,"--- mysum = ",mysum,"indices",hyphen[i],hyphen[i+1])

#hyphen = hyphenation_simple(list_lengths_words,line_length)
#print_hyphenation_simple(list_lengths_words,hyphen)


################################################
def hyphenation_spaces(list_len_words,list_len_line):
    hyphen = [0]
    i = 1

    while i < len(list_len_words):
        mysum = list_len_words[i-1]

        while (i < len(list_len_words)) and (mysum <= list_len_line):
            mysum = mysum + space_length + list_len_words[i]
            i = i + 1
            
        if i < len(list_len_words): 
            hyphen = hyphen + [i-1]

    hyphen = hyphen + [len(list_len_words)]

    return hyphen  




################################################
def print_hyphenation_spaces(list_len_words,hyphen):
    print("\n--- Hyphenation with spaces ---")
    print("list_lengths des words",list_len_words)
    print("hyphen",hyphen)
    for i in range(len(hyphen)-1):
        line = list_len_words[hyphen[i]:hyphen[i+1]]
        nb_spaces = len(line)-1       
        mysum =  sum(line) + nb_spaces*space_length      
        print(i,"---",line,"--- mysum = ",mysum,"indices",hyphen[i],hyphen[i+1])


# hyphen = hyphenation_spaces(list_lengths_words,line_length)
# print_hyphenation_spaces(list_lengths_words,hyphen)



################################################
def compute_spaces_lengths(list_len_words,hyphen,list_len_line):
    list_len_spaces_line = []
    
    for i in range(len(hyphen)-2):

        line = list_len_words[hyphen[i]:hyphen[i+1] ] 
        nb_spaces = len(line)-1
        mysum =  sum(line) + nb_spaces*space_length
        rest = list_len_line - mysum
        if nb_spaces > 0:
            new_space = space_length + rest / nb_spaces
        else:
            new_space = space_length
        list_len_spaces_line = list_len_spaces_line + [new_space]

    list_len_spaces_line = list_len_spaces_line + [space_length] # Last line of paragraph not justified

    return list_len_spaces_line



################################################
def print_compute_list_len_spaces(list_len_words,hyphen,list_len_line):
    list_len_spaces_line = compute_spaces_lengths(list_len_words,hyphen,line_length)
    print("\n--- Hyphenation with spaces ---")
    print("list lengths of words",list_len_words)
    print("hyphen",hyphen)
    for i in range(len(hyphen)-1):
        line = list_len_words[hyphen[i]:hyphen[i+1]]
        nb_spaces = len(line) - 1     
        mysum =  sum(line) + nb_spaces*list_len_spaces_line[i]   

        print(i,"---",line,"--- mysum = ",mysum,"indices",hyphen[i],hyphen[i+1])
        print("list length space of this line",list_len_spaces_line[i])


#hyphen = hyphenation_spaces(list_lengths_words,line_length)
#print_compute_spaces_lengths(list_lengths_words,hyphen,line_length)




