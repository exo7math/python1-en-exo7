
##############################
# Random blocks
##############################

from random import *
from tkinter import *
import time 

##############################
# Activity 3 - Circular movement
##############################

n = 10   # nb of lines
p = 10   # nb of columns 
boundary = min(n,p)//5  # distance to the boundary

array = [[0 for j in range(p)] for i in range(n)]

array[(n-1)//2][(p-1)//2] = 1  # center


##################################################
def print_array():
    for i in range(n):
        for j in range(p):
            print(array[i][j], end="")
        print()

    return

# print_array()   

    
##################################################
def can_move(i,j):
    # if array[i][j]:   # on an existing block
    #     return False

    if i>0 and array[i-1][j]:   # above?
        return False

    if i<n-1 and array[i+1][j]:  # below?
        return False

    if j>0 and array[i][j-1]:   # left?
        return False

    if j<p-1 and array[i][j+1]:  # right?
        return False

    return True

##################################################
def is_inside(i,j):
    if (0 <= i < n) and (0 <= j < p):
        return True
    else:
        return False 


##################################################
def launch_one_block():
    i = randint(0+boundary,n-1-boundary)
    j = randint(0+boundary,p-1-boundary)

    while is_inside(i,j) and can_move(i,j):
        dx = randint(-1,1)
        dy = randint(-1,1)
        i = i + dx
        j = j + dy

    if is_inside(i,j):
        array[i][j] = 1

    return i,j


##################################################
def launch_blocks(k):
    for __ in range(k):
        launch_one_block()

    return

launch_blocks(5)



##############################
# Static tlinter display
##############################

n = 30   # nb of lines
p = 30   # nb of columns

boundary = min(n,p)//10  # distance to boundary for launch
scale = 20

array = [[0 for j in range(p)] for i in range(n)]

array[(n-1)//2][(p-1)//2] = 1  # center

nb_blocks = 10

root = Tk()  

canvas = Canvas(root, width=p*scale, height=n*scale, background="white")
canvas.pack(fill="both", expand=True)


def display_array():
    canvas.delete("all")   # clear all

    for i in range(n):
        for j in range(p):
            if array[i][j]:
                canvas.create_rectangle(j*scale,i*scale,j*scale+scale-1,i*scale+scale-1,width=1,fill='green')
    return



def action_block():
    launch_blocks(nb_blocks)
    display_array()

    return

button_block = Button(root,text="Launch blocks", width=20, command=action_block)
button_block.pack(pady=10)

button_quit = Button(root,text="Quit", width=20, command=root.quit)
button_quit.pack(side=BOTTOM, pady=10)

root.mainloop()

