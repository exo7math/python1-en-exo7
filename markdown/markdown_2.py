
##############################
# Text viewer - Markdown
##############################


##############################
# Activity 2 - Afficher du markdown
##############################


from tkinter import *
from tkinter.font import Font


##############################
# From activity 1
##############################

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




def font_choice(mode,in_bold,in_italics):
    """ Return a font depending on the parameters
    Input: a mode (among: text, list, title, subtitle,...), bold or not, italic or not
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


##################################################
## Question 1 ##

def print_line_v1(par,posy):
    """ Display some text on one line without any formating
    Input: a paragraph (i.e. a long line), the vertical position
    Output: display """   

    posx = 20  # Start on the left of the window

    list_words = par.split()
    for word in list_words:

        word = word + " " # Add a space between words

        word_canvas = canvas.create_text(posx,posy, text=word,anchor=SW,font=font_title,fill=text_color)
        canvas.create_rectangle(canvas.bbox(word_canvas),width=2)

        # New x position for the next word
        posx = canvas.bbox(word_canvas)[2]

    return 

# Tests
# print_line_v1("Hello, this is my first text!",100)
# root.mainloop()


##################################################
## Question 2 ##

def print_line_v2(par,posy):
    """ Print the text on one line with respect to some mode:title, subtitle, text, list
    Input: a paragraph (a long line, the vertical position
    Output: display """ 

    # Default mode: text without indent
    mode = "text"
    indentation = 20

    if par[0:2] == "##":       # Subtitle
        mode = "subtitle"
        par = par[2:]          # Delete the ##
    elif par[0] == "#":        # Title
        mode = "title"
        par = par[1:]          # Delete the #       
    elif par[0] == "+":        # List
        mode = "list"
        par = u'\u2022' + par[1:]          # Replace the "+" by a bullet
        indentation = 40

    
    # Start the line (indent if list)
    posx = indentation

    list_words = par.split()
    for word in list_words:

        myfont = font_choice(mode,False,False)

        word = word + " "   # Add a space between words
        word_canvas = canvas.create_text(posx,posy, text=word,anchor=SW,font=myfont,fill=text_color)
        posx = canvas.bbox(word_canvas)[2]

    return


# Tests
print_line_v2("# Here is a title",80)
print_line_v2("## And here a subtitle",115)
print_line_v2("Normal text and, below, a list:",150)
print_line_v2("+ Apple",175)
print_line_v2("+ Banana",200)
print_line_v2("+ Cherry",225)
root.mainloop()


##################################################
## Question 3 ##

def print_line_v3(par,posy):
    """ Display text that maybe bold
    Input: a paragraph (a long line, the vertical position
    Output: display """ 

    mode = "text"
    indentation = 20

    if par[0:2] == "##":       # Subtitle
        mode = "subtitle"
        par = par[2:]          # Delete the ##
    elif par[0] == "#":        # Title
        mode = "title"    
        par = par[1:]          # Delete the #       
    elif par[0] == "+":        # List
        mode = "liste"
        par = u'\u2022' + par[1:]          # Replace the "+" by a bullet
        indentation = 40

    # Bold / not bold (default not bold, not italic)
    in_bold = False
    in_italics = False
   
    # Start of the line (with more indentation within a list)
    posx = indentation

    list_words = par.split()
    for word in list_words:

        if word == "**":  # Switch bold / not bold
            in_bold = not(in_bold) 
            word = ""           

        if in_bold:
            myfont = font_bold

        if word == "*":       # Switch italic / not italic
            in_italics = not(in_italics)          
            word = ""         

        myfont = font_choice(mode,in_bold,in_italics) 

        if word != "":
            word = word + " " # Space between words
        word_canvas = canvas.create_text(posx,posy, text=word,anchor=SW,font=myfont,fill=text_color)
        posx = canvas.bbox(word_canvas)[2]

    return


# Tests
print_line_v3("These ** words are in bold ** but these * ones are in italics *",100)
print_line_v3("+ Apples and also ** bananas ** but * no cherries *",125)
root.mainloop()



##################################################
## Question 4 ##


# Interline
space_between_lines = 18


def print_paragraph(par,posy):
    """ Display text that maybe bold
    Input: a paragraph (a long line, the vertical position
    Output: display """ 

    mode = "text"
    indentation = 20

    if par[0:2] == "##":       # Subtitle
        mode = "subtitle"
        par = par[2:]          # Delete the ##
    elif par[0] == "#":        # Title
        mode = "title"    
        par = par[1:]          # Delete the #       
    elif par[0] == "+":        # List
        mode = "liste"
        par = u'\u2022' + par[1:]          # Replace the "+" by a bullet
        indentation = 40

    # Bold / not bold (default not bold, not italic)
    in_bold = False
    in_italics = False
   
    # Start of the line (with more indentation within a list)
    posx = indentation

    list_words = par.split()
    for word in list_words:

        if word == "**":  # Switch bold / not bold
            in_bold = not(in_bold) 
            word = ""           

        if in_bold:
            myfont = font_bold

        if word == "*":       # Switch italic / not italic
            in_italics = not(in_italics)          
            word = ""         

        myfont = font_choice(mode,in_bold,in_italics) 

        if word != "":
            word = word + " " # Space between words
        word_canvas = canvas.create_text(posx,posy, text=word,anchor=SW,font=myfont,fill=text_color)
        posx = canvas.bbox(word_canvas)[2]

        if posx > text_width:
            posx = indentation
            posy = posy + space_between_lines

    return posy

# Tests
# print_paragraph("# The title",80)
# print_paragraph("## and its subtitle",115)
# print_paragraph("Hello world!"*5,150)
# print_paragraph("Text ** bold ** normal * italic * normal again "*2,175)
# print_paragraph("+ Apple",200)
# print_paragraph("+ Banana",225)
# print_paragraph("+ Cherry",250)

# long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec dui ac sem molestie viverra quis sit amet felis. Donec felis mi, tempus in laoreet non, pellentesque non sem. Praesent pretium mi at odio congue eleifend. Integer magna neque, feugiat a commodo eget, malesuada in velit. Donec ac orci quis eros molestie lacinia. Sed nisi mi, pretium et tellus eget, dignissim venenatis felis. Mauris sit amet ex in metus ornare cursus non nec sapien."
# print_paragraph(long_text*2,400)

# root.mainloop()




##################################################
## Question 5 ##

def print_file(filename):
    """ Display the paragraphs from a text file
    Input: a filename of a text file with markdown syntax
    Output: display """ 

    # Open file
    fi = open(filename,"r") 
    list_paragraphs = fi.readlines()
    fi.close()

    posy = 50

    # Display each paragraphs
    for par in list_paragraphs:
        newposy = print_paragraph(par,posy)
        posy = newposy + space_between_lines
    
    root.mainloop()

    return


# Tests
print_file("markdown1.md")
# print_file("markdown2.md")