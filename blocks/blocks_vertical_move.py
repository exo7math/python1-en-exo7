
##############################
# Random blocks
##############################

from random import *
from tkinter import *
import time 

##############################
# From activity 1
##############################


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


##############################
# Activity 3 - Dynamic display with tkinter
##############################

n = 50   # nb of lines
p = 100  # nb of columns 
scale = 10
array = [[0 for j in range(p)] for i in range(n)]

tempo = 100 # milli-seconds

list_blocks = []

topline = False # has the top line been reached?

root = Tk()  

canvas = Canvas(root, width=p*scale, height=n*scale, background="white")
canvas.pack(fill="both", expand=True)


def rain_blocks():
    global array, list_blocks, topline
    new_list_blocks = []  # only falling blocks
    for n in range(len(list_blocks)):
        i,j,block = list_blocks[n]
        if can_fall(i,j):
            array[i][j] = 0
            i = i + 1
            array[i][j] = 1
            canvas.coords(block,j*scale,i*scale,j*scale+scale-1,i*scale+scale-1)
            list_blocks[n] = (i,j,block)
            new_list_blocks = new_list_blocks + [(i,j,block)]
        else:
            if i == 0:
                topline = True
    # print('blocks',list_blocks)
    # print('new',new_list_blocks)
    list_blocks = new_list_blocks[:]
    return


def action_block():

    global list_blocks
    i = 0
    j = randint(0,p-1)
    block = canvas.create_rectangle(j*scale,i*scale,j*scale+scale-1,i*scale+scale-1,width=1,fill='green')
    list_blocks = list_blocks + [(i,j,block)]
    rain_blocks()
    if not(topline): # if the top line has not been reached
        canvas.after(tempo,action_block) # call again after a small time period
    return

    

button_block = Button(root,text="Start", width=20, command=action_block)
button_block.pack(pady=10)

button_quit = Button(root,text="Quit", width=20, command=root.quit)
button_quit.pack(side=BOTTOM, pady=10)

root.mainloop()

# print_array()



