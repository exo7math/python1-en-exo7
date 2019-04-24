
##############################
# Aléatoire
##############################

from random import *
from tkinter import *
import time 

##############################
# Activity 1 - Blocks falling
##############################

n = 4   # nb of lines
p = 6   # nb of columns 

array = [[0 for j in range(p)] for i in range(n)]

array[3][3] = 1
array[3][2] = 1
array[2][2] = 1
array[1][2] = 1
array[0][4] = 1

##################################################
def print_array():

    for i in range(n):
        for j in range(p):
            print(array[i][j], end="")
        print()

    return

print_array()   

    
##################################################
def can_fall(i,j):
    if i == n-1:      # bottom line?
        return False

    if array[i+1][j]:  # cell just below?
        return False
    
    if j>0 and array[i][j-1]:   # block on the left?
        return False

    if j<p-1 and array[i][j+1]:  # block on the right?
        return False

    return True



##################################################
def drop_one_block(j):
    i = 0
    while can_fall(i,j):
        i = i + 1

    array[i][j] = 1

    return i,j


##################################################
def drop_blocks(k):
    # print_array()
    # print()
    for __ in range(k):
        j = randint(0,p-1)
        drop_one_block(j)
        # print_array()
        # print()

    return


# drop_blocks(7)
# print()
# print_array()

# exit()

##############################
# Activity 2 - tkinter static display
##############################

n = 25   # nb of lines
p = 50   # nb of columns 

array = [[0 for j in range(p)] for i in range(n)]

scale = 20  # scale 
nb_blocks = 50

root = Tk()  

canvas = Canvas(root, width=p*scale, height=n*scale, background="white")
canvas.pack(fill="both", expand=True)


def display_array():
    canvas.delete("all")   # Clear all

    for i in range(n):
        for j in range(p):
            if array[i][j]:
                canvas.create_rectangle(j*scale,i*scale,j*scale+scale-1,i*scale+scale-1,width=1,fill='green')
    return

# Test
# display_array()

def action_blockk():
    drop_blocks(nb_blocks)
    display_array()

    return

button_block = Button(root,text="View blocks", width=20, command=action_blockk)
button_block.pack(pady=10)

button_quit = Button(root,text="Quit", width=20, command=root.quit)
button_quit.pack(side=BOTTOM, pady=10)

root.mainloop()

