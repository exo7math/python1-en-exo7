
##############################
# Text viewer - Markdown
##############################


##############################
# Lesson tkinter
##############################


from tkinter import *
from tkinter.font import Font

# tkinter window
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Font
myfont = Font(family="Times", size=30)

# Some text
canvas.create_text(100,100, text="Text with Python!",anchor=SW,font=myfont,fill="blue")


# Font
myfont = Font(family="Courier", weight="bold",size=30)

# Some text
canvas.create_text(100,200, text="Bold text",anchor=SW,font=myfont,fill="black")


# Font
myfont = Font(family="Helvetica", slant="italic",size=30)

# Some text
canvas.create_text(100,300, text="Italic text",anchor=SW,font=myfont,fill="red")



# Bounding box

# Font
myfont = Font(family="Courier", weight="bold",size=30)

# Some text
mytext = canvas.create_text(400,400, text="Text in a box",anchor=SW,font=myfont,fill="red")

# Coordinates of the bounding rectangle (x1,y1,x2,y2)
x1,y1,x2,y2 = canvas.bbox(mytext)

# Display the bounding box
canvas.create_rectangle(x1,y1,x2,y2,width=2)

# Launch the window
root.mainloop()
