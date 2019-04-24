
##############################
# Game of life
##############################

##############################
# From previous activities
##############################


from tkinter import *

# Window tkinter
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Default: nothing
n, p = 25, 25
scale = 40
n, p = 30, 40
scale = 20

array = [[0 for j in range(p)] for i in range(n)] 


##################################################

def number_neighbors(i,j,array):
    """ Compute the nb of living neighbors of the box (i,j)
    Input: a box position in a array of cells
    Output: the nb of neighbor cells """ 

    nb = 0
    # Neighbor top left
    if (i>0) and (j>0) and (array[i-1][j-1] != 0):
        nb += 1
    # Neighbor just above
    if (i>0) and (array[i-1][j] != 0):
        nb += 1
    # Neighbor top right
    if (i>0) and (j<p-1) and (array[i-1][j+1] != 0):
        nb += 1
    # Neighbor left
    if (j>0) and (array[i][j-1] != 0):
        nb += 1
    # Neighbor rigth
    if (j<p-1) and (array[i][j+1] != 0):
        nb += 1
   # Neighbor left below
    if (i<n-1) and (j>0) and (array[i+1][j-1] != 0):
        nb += 1
    # Neighbor just below
    if (i<n-1) and (array[i+1][j] != 0):
        nb += 1
    # Neighbor right below
    if (i<n-1) and (j<p-1) and (array[i+1][j+1] != 0):
        nb += 1

    return nb

def evolution(array):
    """ Caompute the evolution to the next day
    Input: an array
    Output: an array """    

    new_array = [[0 for j in range(p)] for i in range(n)]

    for j in range(p):
        for i in range(n):
            # Cell alive or not?
            if array[i][j] != 0:
                cellule_alive = True
            else:
                cellule_alive = False

            # Nombres de neighbors
            nb_neighbors = number_neighbors(i,j,array)

            # Règle du jeu de la vie
            if cellule_alive == True and (nb_neighbors == 2 or nb_neighbors == 3):
                new_array[i][j] = 1
            if cellule_alive == False and nb_neighbors == 3:
                new_array[i][j] = 1          

    return new_array

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

def draw_array(array):
    """ Display an array on a graphical screen
    Input: an array
    Output: nothing (display on scree) """    

    for i in range(n):
        for j in range(p):
            if array[i][j] != 0:
                canvas.create_rectangle(j*scale,i*scale,(j+1)*scale,(i+1)*scale,fill="red")
        
    return


##############################
# Activity 4 - Game of life: full program
##############################

##################################################
## Question 0 ##

# Blinker
def blinker():
    """ blinker definition """
    global array
    array = [[0 for j in range(p)] for i in range(n)] 
    array[4][7] = 1
    array[4][8] = 1
    array[4][9] = 1
    canvas.delete("all")   
    draw_grid()   
    draw_array(array)
    return


# Spaceship
def spaceship():
    """ Spaceship definition """
    global array
    array = [[0 for j in range(p)] for i in range(n)] 
    array[3][4] = 1
    array[3][5] = 1
    array[3][6] = 1
    array[2][6] = 1
    array[1][5] = 1
    canvas.delete("all")    
    draw_grid()   
    draw_array(array)
    return


# Pentadecathlon
def pentadecathlon():
    """ pentadecathlon definition """
    global array
    array = [[0 for j in range(p)] for i in range(n)] 
    array[6][4] = 1
    array[6][5] = 1
    array[6][7] = 1
    array[6][8] = 1    
    array[6][9] = 1
    array[6][10] = 1
    array[6][12] = 1
    array[6][13] = 1  
    array[5][6] = 1
    array[7][6] = 1
    array[5][11] = 1
    array[7][11] = 1 
    canvas.delete("all")      
    draw_grid()                    
    draw_array(array)
    return


##################################################
## Question 1 ##

# Boutons

def action_button_evolution():
    global array
    array = evolution(array)
    canvas.delete("all")
    draw_grid()
    draw_array(array)
    return


button_quit = Button(root,text="Quit", width=8, command=root.quit)
button_quit.pack(side=BOTTOM, padx=5, pady=20)

button_display = Button(root,text="Evolve", width=20, command=action_button_evolution)
button_display.pack(side=BOTTOM, padx=5, pady=20)

button_blinker = Button(root,text="Blinker", width=20, command=blinker)
button_blinker.pack(side=TOP, padx=5, pady=5)

button_spaceship = Button(root,text="Spaceship", width=20, command=spaceship)
button_spaceship.pack(side=TOP, padx=5, pady=5)

button_pentadecathlon = Button(root,text="Pentadecathlon", width=20, command=pentadecathlon)
button_pentadecathlon.pack(side=TOP, padx=5, pady=5)


# root.mainloop()


##################################################
## Question 2 ##

def on_off(i,j):
    """ Change the state of one cell """
    global array
    if array[i][j] == 0:
        array[i][j] = 1
    else: 
        array[i][j] = 0
    return


def xy_to_ij(x,y):
    """ Coordonnites (x,y) to coordinates (i,j) """
    i = y // scale
    j = x // scale
    return i, j


def action_mouse_click(event):
    canvas.focus_set()
    # print("Clic à", event.x, event.y)
    x = event.x
    y = event.y
    on_off(*xy_to_ij(x,y))
    canvas.delete("all")   
    draw_grid()    
    draw_array(array)
    return

# Link mouse click/action
canvas.bind("<Button-1>",action_mouse_click)

draw_grid()
draw_array(array)
root.mainloop()