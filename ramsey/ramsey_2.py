
##############################
# Ramsey graphs and combinatorics
##############################



##############################
# Activity 2 - Graphic display
##############################


from tkinter import *
from math import *
from tkinter.font import Font


from ramsey_1 import *  # For examples

# tkinter window
root = Tk()

canvas = Canvas(root, width=800, height=500, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Scale
scale = 200


# Basic version (compute many times the same thing)
##################################################
def display_graph_basic(array):
    """
    Display a graph
    Input: a graph
    Output: nothing
    """    
    n = len(array)

    # Edges
    for j in range(n):
        for i in range(n):
            xi = 2*scale + cos(2*i*pi/n)*scale
            yi = 1.5*scale + sin(2*i*pi/n)*scale
            xj = 2*scale + cos(2*j*pi/n)*scale
            yj = 1.5*scale + sin(2*j*pi/n)*scale        
            if array[i][j] == 0:
                canvas.create_line(xi,yi,xj,yj,width=4,fill="red") 
            if array[i][j] == 1:
                canvas.create_line(xi,yi,xj,yj,width=4,fill="green") 

    # Vertices                 
    for i in range(n):
        x = 2*scale + cos(2*i*pi/n)*scale
        y = scale + sin(2*i*pi/n)*scale
        canvas.create_oval(x-5,y-5,x+5,y+5,fill="black")

    return


# Optimal version
##################################################
def display_graph(array):
    """
    Display a graph
    Input: a graph
    Output: nothing
    """   
    n = len(array)  # Number of vertices

    # List of the coordinates (x,y) of the vertices
    coord = [(2*scale + cos(2*i*pi/n)*scale,1.2*scale + sin(2*i*pi/n)*scale) for i in range(n)]

    # Edges
    for j in range(n):
        for i in range(j+1,n):  # i>j
            if array[i][j] == 0:
                canvas.create_line(coord[i],coord[j],width=4,fill="red",dash=(6, 2)) 
            if array[i][j] == 1:
                canvas.create_line(coord[i],coord[j],width=4,fill="green")

    myfont = Font(family="Courier", weight="bold",size=18)
     # Vertices                  
    for i in range(n):
        x,y = coord[i]
        canvas.create_oval(x-15,y-15,x+15,y+15,fill="black")
        canvas.create_text(x,y,text=str(i),font=myfont,fill="white")


    return

# Launch of the window
if __name__ == '__main__':
    button_quit = Button(root,text="Quit", width=8, command=root.quit)
    button_quit.pack(side=BOTTOM, padx=5, pady=20)

    # Example
    display_graph(example_graph_4)
    root.mainloop()

