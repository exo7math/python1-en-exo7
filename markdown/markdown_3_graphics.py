

##############################
# Text viewer - Markdown
##############################

##############################
# Activity 3 - Justify text
##############################

from random import randint
list_lengths = [randint(5,15) for i in range(50)] 
#list_lengths = [14, 3, 16, 9, 2, 11, 13, 5, 4, 19, 16, 6, 17, 16, 15, 5, 14, 12, 17, 7]
list_lengths = [8, 11, 9, 14, 8, 8, 15, 10, 14, 11, 15, 15, 5, 12, 9, 9, 15, 10, 14, 5, 12, 8, 8, 13, 10, 11, 8, 13, 7, 5, 6, 11, 7, 7, 13, 6, 6, 9, 8, 12, 5, 8, 7, 6, 6, 15, 13, 11, 7, 12]

line_length = 100
space_length = 1


##############################
# Graphic version
##############################

from tkinter import *
from tkinter.font import Font


# tkinter window
root = Tk()
        
canvas = Canvas(root, width=900, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Page and text format
scale = 6
text_width = line_length * scale
text_height = 250

# Text background
canvas.create_rectangle(100,120,100+text_width,100+text_height,width=2)


## Question 0 ##  

## Hyphenation as with Markdown: only after a word exceed the line

################################################
def hyphenation_exceed(list_len):

    hyphen = [0]

    i = 0
    mysum  = 0
    while i < len(list_len):
        
        mysum += list_len[i]

        if mysum >= line_length:
            hyphen += [i+1]
            mysum = 0

        i += 1

    hyphen += [len(list_len)]

    return hyphen 


################################################
def print_hyphenation_exceed():
    print("\n--- Hyphenation when exceeding the end of the line ---")
    print("Length of words :",list_lengths)

    hyphen = hyphenation_exceed(list_lengths)   
    print("hyphen",hyphen)

    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        mysum = sum(line)
        print("\nLine",i,":",line,"\nIndex",hyphen[i],"to",hyphen[i+1]-1,"= list_len[",hyphen[i],":",hyphen[i+1],"]","\nSum =",mysum,"Remainder =",line_length-mysum,)

    return




# Test
# print_hyphenation_exceed()


################################################
def print_line(line,posy,space):
    posx = 100
    for list_len in line:
        canvas.create_rectangle(posx,posy,posx+list_len*scale,posy+20,width=2,outline='red')
        canvas.create_text(posx+5,posy+4,anchor=NW,text=str(list_len),fill="blue")

        posx = posx + list_len*scale + space*scale

        nb_spaces = len(line)-1
        mysum = sum(line)+nb_spaces*space

        canvas.create_text(100+text_width+50,posy+4,anchor=NW,text="sum = "+str(mysum),fill="red")
    return


################################################
def graphic_hyphenation_exceed():

    hyphen = hyphenation_exceed(list_lengths)   

    posy = 150
    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        print_line(line,posy,0)
        posy  += 30
    root.mainloop()
    return

# Test
# graphic_hyphenation_exceed()


## Question 1 ##

################################################
def hyphenation_simple(list_len):

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
def print_hyphenation_simple():
    print("\n--- Hyphenation without spaces ---")
    print("Length of words:",list_lengths)

    hyphen = hyphenation_simple(list_lengths)   
    print("Hyphenation:",hyphen)

    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        mysum = sum(line)
        print("\nLine",i,":",line,"\nIndex",hyphen[i],"to",hyphen[i+1]-1,"= list_len[",hyphen[i],":",hyphen[i+1],"]","\nSum =",mysum,"Remainder =",line_length-mysum,)

    return

# Test
# print_hyphenation_simple()





################################################
def graphic_hyphenation_simple():

    hyphen = hyphenation_simple(list_lengths)   

    posy = 150
    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        print_line(line,posy,0)
        posy  += 30
    root.mainloop()
    return

# Test
# graphic_hyphenation_simple()




## Question 2 ##

################################################
def hyphenation_spaces(list_len):

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
def print_hyphenation_spaces():
    print("\n--- Hyphenation with spaces ---")
    print("Length of words :",list_lengths)

    hyphen = hyphenation_spaces(list_lengths) 
    print("Hyphenation :",hyphen)

    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        nb_spaces = len(line)-1       
        mysum =  sum(line) + nb_spaces*space_length      
        print("\nLine",i,":",line,"\nIndex",hyphen[i],"to",hyphen[i+1]-1,"= list_len[",hyphen[i],":",hyphen[i+1],"]","\nSum with spaces =",mysum,"Remainder =",line_length-mysum,)

    return

# Test 
# print_hyphenation_spaces()

################################################
def graphic_hyphenation_spaces():

    hyphen = hyphenation_spaces(list_lengths)   

    posy = 150
    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        print_line(line,posy,space_length)
        posy  += 30
    root.mainloop()
    return

# Test
# graphic_hyphenation_spaces()


## Question 3 ##

################################################
def compute_space_lengths(list_len,hyphen):

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

    # Dernière line du paragraphe pas justifiée
    list_space_lengths += [space_length] 

    return list_space_lengths



################################################
def print_space_lengths():


    print("\n--- Hyphenation with spaces et justification ---")
    print("Length of words:",list_lengths)

    hyphen = hyphenation_spaces(list_lengths) 
    print("Hyphenation:",hyphen)

    list_space_lengths = compute_space_lengths(list_lengths,hyphen)
    print("Length of spaces for each line:",[float("{0:0.2f}".format(l)) for l in list_space_lengths])

    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        nb_spaces = len(line) - 1     
        mysum =  sum(line) + nb_spaces*list_space_lengths[i]   

        print("\nLine",i,":",line,"\nIndex",hyphen[i],"to",hyphen[i+1]-1,"= list_len[",hyphen[i],":",hyphen[i+1],"]","\nSum with spaces =",mysum,"Remainder =",line_length-mysum,)
        print("Length of the spaces for this line",list_space_lengths[i])

    return

# Test
print_space_lengths()



################################################
def graphic_hyphenation_justification():

    hyphen = hyphenation_spaces(list_lengths)
    list_space_lengths = compute_space_lengths(list_lengths,hyphen) 

    posy = 150
    for i in range(len(hyphen)-1):
        line = list_lengths[hyphen[i]:hyphen[i+1]]
        print_line(line,posy,list_space_lengths[i])
        posy  += 30
    root.mainloop()
    return

# Test
graphic_hyphenation_justification()

