
##############################
# Game of life
##############################


##############################
# From Activity 1
##############################

n, p = 5, 8;
array = [[0 for j in range(p)] for i in range(n)] 

# Blinker
array[2][2] = 1
array[2][3] = 1
array[2][4] = 1


##############################
# Activity 2 - Graphic display
##############################

##################################################
## Question 1 ##

from tkinter import *

# Window tkinter
root = Tk()

canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Scale 
scale = 100


def draw_grid():
    """ Show the grid """    

    for i in range(n+1):
        canvas.create_line(0,i*scale,p*scale,i*scale)

    for j in range(p+1):
        canvas.create_line(j*scale,0,j*scale,n*scale)
        
    for i in range(n):
        canvas.create_text(scale//3,i*scale+scale//2,text=str(i)) 

    for j in range(p):        
        canvas.create_text(j*scale+scale//2,scale//3,text=str(j)) 

    return


##################################################
## Question 2 ##

def draw_array(array):
    """ Display an array on a graphical screen
    Input: an array
    Output: nothing (display on scree) """    

    for i in range(n):
        for j in range(p):
            if array[i][j] != 0:
                canvas.create_rectangle(j*scale,i*scale,(j+1)*scale,(i+1)*scale,fill="red")
        
    return


# Boutons
def action_button_display():
    canvas.delete("all")
    draw_grid()
    draw_array(array)
    return


button_quit = Button(root,text="Quit", width=8, command=root.quit)
button_quit.pack(side=BOTTOM, padx=5, pady=20)

button_display = Button(root,text="View", width=30, command=action_button_display)
button_display.pack(side=BOTTOM, padx=5, pady=20)

# Test
draw_grid()
draw_array(array)
root.mainloop()




