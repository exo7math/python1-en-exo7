
##############################
# Statistics -- Data visualization -- tkinter
##############################


##############################
# Lesson tkinter - Buttons
##############################


from tkinter import *
from random import *

root = Tk()     
canvas = Canvas(root, width=400, height=200, background="white")
canvas.pack(fill="both", expand=True)

def action_button():
    canvas.delete("all")       # Clear all
    colors = ["red","orange","yellow","green","cyan","blue","violet","purple"]
    col = choice(colors)      # Random color
    canvas.create_rectangle(100,50,300,150,width=5,fill=col)
    return

button_color = Button(root,text="View", width=20, command=action_button)
button_color.pack(pady=10)

button_quit = Button(root,text="Quit", width=20, command=root.quit)
button_quit.pack(side=BOTTOM, pady=10)

root.mainloop()

