
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



##############################
# Activity 4 - Tkinter dynamic display
##############################


n = 20   # nb of lines
p = 20   # nb of columns

boundary = min(n,p)//10  # distance to boundary for launch
scale = 20
tempo = 20 # milli-seconds

array = [[0 for j in range(p)] for i in range(n)]

array[(n-1)//2][(p-1)//2] = 1  # center

block_out = False # is the boundary reached?

root = Tk()  

canvas = Canvas(root, width=p*scale, height=n*scale, background="white")
canvas.pack(fill="both", expand=True)

def move_block():
    global i,j,array,block

    if is_inside(i,j) and can_move(i,j): 
        dx = randint(-1,1)
        dy = randint(-1,1)
        array[i][j] = 0
        i = i + dx
        j = j + dy
        if is_inside(i,j):
            array[i][j] = 1    
            canvas.coords(block,j*scale,i*scale,j*scale+scale-1,i*scale+scale-1)
            canvas.after(tempo,move_block)
        else:
            canvas.delete(block)



def launch_one_block():
    global i,j,block,array,block_out

    i = randint(0+boundary,n-1-boundary)
    j = randint(0+boundary,p-1-boundary)
    block = canvas.create_rectangle(j*scale,i*scale,j*scale+scale-1,i*scale+scale-1,width=1,fill='green')

    move_block()
    return


def action_block():
    # Affichage centre
    i = (n-1)//2
    j = (p-1)//2
    canvas.create_rectangle(j*scale,i*scale,j*scale+scale-1,i*scale+scale-1,width=1,fill='green')

    launch_one_block()

    return


button_block = Button(root,text="Launch one block", width=20, command=action_block)
button_block.pack(pady=10)

button_quit = Button(root,text="Quit", width=20, command=root.quit)
button_quit.pack(side=BOTTOM, pady=10)

root.mainloop()




