
##############################
# Statistics -- Data visualization -- tkinter
##############################


##############################
# Activity 4 - Data visualization (bis)
##############################

from math import *
from tkinter import *
from random import *

from statistics_3 import * 


root = Tk()  # tkinter window
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

scale = 15  # Scale to enlarge picture

##################################################
##################################################

def box_plot(grade_count):
    """ Box plot! """

    # Bar graphics
    for i in range(len(grade_count)):  # i range from 0 to 10
        hauteur = grade_count[i] * scale
        canvas.create_rectangle(100+2*i*10,300,100+(2*i+1)*10,300-hauteur,fill="red")
        canvas.create_text(100+2*i*10+5,320,text=str(i),fill="red")

    # Vertical axis on the left
    max_count = max(grade_count)
    canvas.create_line(95,300,95,300-scale*max_count)   
    for j in range(max_count+1):
        canvas.create_line(90,300-scale*j,95,300-scale*j)
        canvas.create_text(85,300-scale*j,text=str(j))       

    # Data to a list of grades
    mylist = grades_to_list(grade_count)

    # Computes the quartiles & co
    mini = min(mylist)
    maxi = max(mylist)
    Q1,Q2,Q3 = quartiles(mylist)
    
    #  Diagram
    canvas.create_rectangle(100+2*mini*10+5,197,100+2*Q1*10+5,203,fill="blue")  
    canvas.create_rectangle(100+2*Q1*10+5,185,100+2*Q3*10+5,215,width=3,outline="blue")  
    canvas.create_rectangle(100+2*Q2*10+5-2,185,100+2*Q2*10+5+2,215,fill="blue")     
    canvas.create_rectangle(100+2*Q3*10+5,197,100+2*maxi*10+5,203,fill="blue") 

    return


# Test 
# grade_count = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
grade_count = [0,0,1,2,5,2,3,5,4,1,2]
box_plot(grade_count)
root.mainloop()