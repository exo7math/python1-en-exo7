
##############################
# Test - tkinter - 
##############################

from tkinter import *
from tkinter.font import Font

from hyphenation_project import *



##############################
# From activity 1
##############################

# tkinter window
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Size of the text page
text_width = 700
text_height = 550
indentation = 30 # For lists
line_length = text_width - 10
space_length = 7
space_between_lines = 18

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


def font_choice(mode,in_bold,in_italic):
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
        elif in_italic:
            myfont = font_italic
        else:
            myfont = font_text

    return myfont


##################################################
def format_paragraph(par):

    # Which mode
    if par[0:2] == "##":       # Subtitle
        mode = "subtitle"
        par = par[2:]          # Delete the ##
    elif par[0] == "#":        # Title
        mode = "title"
        par = par[1:]          # Delete the #
    elif par[0] == "+":
        mode = "list"
        par = u'\u2022' + par[1:]    # Repalce "+" by a bullet
    else:
        mode = "text"


    list_format_words = []

    # Bold/italic
    in_bold = False
    in_italic = False

    for word in par.split():
        if word == "**":  # Switch bold / not bold
            in_bold = not(in_bold) 
            word = ""           

        if word == "*":       # Switch italic / not istalic
            in_italic = not(in_italic)          
            word = "" 

        if word != "":
            list_format_words += [[word,mode,in_bold,in_italic]]

    return list_format_words


def length_one_word(word,myfont):
    # 'Display' some invisible text in order to get its length
    word_canvas = canvas.create_text(100,100, text=word,anchor=SW,font=myfont,fill=background_color)

    # Recover extremities
    x1,y1,x2,y2 = canvas.bbox(word_canvas)

    return x2 - x1


##################################################
def lengths_words(list_format_words):
    len_words = []
    for word,mode,in_bold,in_italic in list_format_words:
         fonte = font_choice(mode,in_bold,in_italic)
         len_words += [length_one_word(word,fonte)]

    return len_words



# list_format_words = format_paragraph("Hello WORLD ** Gras **")
# len_words = lengths_words(list_format_words)
# print(list_format_words)
# print(len_words)


##################################################
def print_paragraph(par,posy):

    list_format_words = format_paragraph(par)
    len_words = lengths_words(list_format_words)

    hyphen = hyphenation_spaces(len_words,line_length)
    len_spaces_line = compute_spaces_lengths(len_words,hyphen,line_length)

 
    # Indentatation
    if (len(list_format_words)>0) and (list_format_words[0][1] == "liste"):
        indent = indentation  
    else:
        indent = 20   

    hyphen = hyphenation_spaces(len_words,line_length-indent)
    len_spaces_line = compute_spaces_lengths(len_words,hyphen,line_length-indent)


    posx = indent

    for j in range(len(hyphen)-1):
        line = len_words[hyphen[j]:hyphen[j+1]]


        for i in range(hyphen[j],hyphen[j+1]):
            word,mode,in_bold,in_italic = list_format_words[i]
            fonte = font_choice(mode,in_bold,in_italic)

            # Dispaly a word (visible)
            word_canvas = canvas.create_text(posx,posy, text=word,anchor=SW,font=fonte,fill=text_color)

            posx = posx + len_words[i] + len_spaces_line[j]

        posx = indent
        posy = posy + space_between_lines

    return posy

# Tests
# print_paragraph("Titre Hello World AAAAA AAA "*11,100)
# print_paragraph("## subtitle Hello !"*5,150)
# print_paragraph("Hello !"*30,200)
# print_paragraph("Hello ! ** GRAS **   * Italique *  ** TRES GRAS ** Rien  * Très italique * ** SUPER GRAS **",300)
# print_paragraph("+ Pomme etc "*20,350)
# print_paragraph("+ Poire ou peche "*10,400)
# root.mainloop()

##################################################




  


##################################################
def print_file(filename):

    # Open the file
    fi = open(filename,"r") 
    list_paragraphs = fi.readlines()
    fi.close()

    posy = 50

    # Deal with each paragraph
    for par in list_paragraphs:
        newposy = print_paragraph(par,posy)
        posy = newposy  #+ space_between_lines
    
    root.mainloop()

    return


# Tests
print_file("markdown1.md")

##################################################
##################################################
##################################################
##################################################

