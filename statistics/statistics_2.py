
##############################
# Statistics -- Data visualization -- tkinter
##############################


##############################
# Activity 2 - Data visualization
##############################


##############################
## Question 0 ##

from math import *
from random import *
from tkinter import *

# tkinter window
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

def one_color():
    """ Return a random color
    Input: nothing
    Output: a color """    

    # Method 1 - Limited choice
    # colors = ["red","orange","yellow","green","cyan","blue","violet","purple"]
    # col = random.choice(colors)

    # Methode 2 - "Infinite" choice
    R = randint(0,255)    
    V = randint(0,255)    
    B = randint(0,255)
    col = '#%02x%02x%02x' % (R, V, B)

    return col



##################################################
## Question 1 ##

def bar_graphics(mylist):
    """Bars graphics with one bar for each element of the list """
    posx = 100
    for x in mylist:
        height = x * scale
        canvas.create_rectangle(posx,400,posx+10,400-height,fill="red")
        posx = posx + 30

    # Bonus: vertical axis on the left
    max_mylist = max(mylist)
    canvas.create_line(90,400,90,400-scale*max_mylist)   
    for j in range(max_mylist+1):
        canvas.create_line(85,400-scale*j,90,400-scale*j)
        canvas.create_text(80,400-scale*j,text=str(j)) 

    return


# Test
# scale = 20
# mylist = [5,8,6,3,7,10,4]
# bar_graphics(mylist)
# root.mainloop()


##################################################
## Question 2 ##

def cumulative_graphics(mylist):
    """ Graphics with rectangles one above the others """
    bas = 500
    for x in mylist:
        height = x * scale
        canvas.create_rectangle(100,bas,200,bas-height,fill=one_color())
        bas = bas - height

    # Bonus: vertical axis on the left
    max_mylist = sum(mylist)
    canvas.create_line(90,500,90,500-scale*max_mylist)   
    for j in range(0,max_mylist+1,5):
        canvas.create_line(85,500-scale*j,90,500-scale*j)
        canvas.create_text(80,500-scale*j,text=str(j)) 
    
    return

# Test
# scale = 5
# mylist = [5,8,6,3,7,10,4,12]
# cumulative_graphics(mylist)
# root.mainloop()

##################################################
## Question 3 ##

def percentage_graphics(mylist):
    """ Rectangular graphics divided by sub-recatngles """
    mysum = sum(mylist)
    posx = 100
    for x in mylist:
        largeur = x/mysum*100 * 5
        canvas.create_rectangle(posx,300,posx+largeur,200,fill=one_color())
        posx = posx + largeur

    # Bonus: horizontal axis below
    canvas.create_line(100,325,600,325)   
    for i in range(0,11):
        canvas.create_line(100+i*50,325,100+i*50,330)
        canvas.create_text(100+i*50,340,text=str(i*10)+"%") 
    return    

# Test
# scale = 5
# mylist = [5,8,6,3,7,10,4,12]
# percentage_graphics(mylist)
# root.mainloop()

##################################################
## Question 4 ##

def sector_graphics(mylist):
    """ Circular graphics divided by sectors """
    mysum = sum(mylist)
    start_angle = 0
    for x in mylist:
        angle = x/mysum*360 
        canvas.create_arc(200,100,550,450,start=start_angle,extent=angle,style=PIESLICE,fill=one_color())
        start_angle = start_angle + angle
    return


# Test
# scale = 5
# mylist = [5,8,6,3,7,10,4,12]
# sector_graphics(mylist)
# root.mainloop()

##################################################
## Question 5 ##

# mylist = [randint(5,15) for i in range(10)] 

mylist = [15,8,6,13,17,10,14,12]

def action_bouton1():
    global scale
    scale = 15
    canvas.delete("all")
    bar_graphics(mylist)
    return

def action_bouton2():
    global scale
    scale = 4
    canvas.delete("all")
    cumulative_graphics(mylist)
    return

def action_bouton3():
    canvas.delete("all")
    percentage_graphics(mylist)
    return

def action_bouton4():
    canvas.delete("all")
    sector_graphics(mylist)
    return

def new_list():
    """ Create a new random list of data """
    global mylist
    n = randint(3,10)
    mylist = [randint(1,20) for i in range(n)] 
    canvas.delete("all")   
    return    

# Titre
root.title("Data visualization")

# Boutons
bouton_quit = Button(root,text="Quit", width=8, command=root.quit)
bouton_quit.pack(side=BOTTOM, padx=5, pady=20)

bouton_new = Button(root,text="New data", width=30, command=new_list)
bouton_new.pack(side=BOTTOM, padx=5, pady=20)

bouton1 = Button(root,text="Bar graphics", width=30, command=action_bouton1)
bouton1.pack(padx=5, pady=20)

bouton2 = Button(root,text="Cumulative graphics", width=30, command=action_bouton2)
bouton2.pack(padx=5, pady=20)

bouton3 = Button(root,text="Percentage graphics", width=30, command=action_bouton3)
bouton3.pack(padx=5, pady=20)

bouton4 = Button(root,text="Sector graphics", width=30, command=action_bouton4)
bouton4.pack(padx=5, pady=20)

root.mainloop()