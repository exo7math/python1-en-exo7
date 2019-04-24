
##############################
# Text viewer - Markdown
##############################


##############################
# Activity 1 - Afficher du text
##############################

##################################################
## Question 1 ##

from tkinter import *
from tkinter.font import Font

# tkinter window
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Size of the text page
text_width = 700
text_height = 500

# Colors
background_color = "lightgray"
text_color = "black"

# Box for the text
canvas.create_rectangle(10,10,text_width,text_height,width=2,fill=background_color)

# Fonts
font_text = Font(family="Times", size=12)
font_italic = Font(family="Times", slant="italic", size=12)
font_bold = Font(family="Times", weight="bold", size=12)
font_title = Font(family="Times", weight="bold", size=20)
font_subtitle = Font(family="Times", weight="bold", size=16)

# Test
# canvas.create_text(100,100, text="Math is fun.",anchor=SW,font=font_title,fill=text_color)
# canvas.create_text(200,200, text="Python is cool!",anchor=SW,font=font_subtitle,fill="red")
# root.mainloop()



##################################################
## Question 2 ##

def text_word(word,myfont):
    """ Put a word in a box
    Input: a string and a font
    Output: display the word and its bounding box """    

    # Display the text
    word_canvas = canvas.create_text(100,100, text=word,anchor=SW,font=myfont,fill=text_color)

    # Coordinates of the rectangle (x1,y1,x2,y2)
    x1,y1,x2,y2 = canvas.bbox(word_canvas)

    # Display the bounding box
    canvas.create_rectangle(x1,y1,x2,y2,width=2)
 
    return

# Test 
# text_word("Some text with a bounding box",font_title)
# root.mainloop()



##################################################
## Question 3 ##

def length_word(word,myfont):
    """ Length of a word
    Input: a string and a font
    Output: the length of the text in pixel """    

    # 'Display' some invisible text in order to get its length
    word_canvas = canvas.create_text(100,100, text=word,anchor=SW,font=myfont,fill=background_color)

    # Recover extremities
    x1,y1,x2,y2 = canvas.bbox(word_canvas)

    return x2 - x1


# Test 
print("Length of the word 'Hello' :",length_word("Hello",font_title),"pixels")
text_word("Hello",font_title)
root.mainloop()



##################################################
## Question 4 ##

def font_choice(mode,in_bold,in_italics):
    """ Return a font depending on the paramters
    Input: a mode (text, list, title, subtilt), bold or not, italic or not
    Output: the font """    

    if mode == "title":
        myfont = font_title
    elif mode == "subtitle":
        myfont = font_subtitle
    else:       # Mode text ou liste
        if in_bold:
            myfont = font_bold
        elif in_italics:
            myfont = font_italic
        else:
            myfont = font_text

    return myfont


# Test 
# myfont = font_choice("Text",False,True)
# canvas.create_text(100,100, text="This is italic",anchor=SW,font=myfont,fill=text_color)
# root.mainloop()

##################################################
