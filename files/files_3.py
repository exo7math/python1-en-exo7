
##############################
# Files
##############################

import os

##############################
# Activity 3 - Images
##############################


## Question 1 ##

def write_image_bw():

    # Create a file to write
    filename = "image_bw.pbm"
    fi = open(filename,"w")

    # Header
    fi.write("P1\n")  # Black and white image
    nb_col = 300
    nb_lin = 200
    fi.write(str(nb_col) + " " + str(nb_lin) + "\n")


    for i in range(nb_lin):
        line = ""
        for j in range(nb_col):
            col = (i+j)//10 % 2
            line = line + str(col) + " "
        line = line + "\n"

        # Write the line
        fi.write(line)

    # Close file
    fi.close()

    return
# Test

print("--- File 'image_bw.pbm' ---")
write_image_bw()


## Question 2 ##

def write_image_gray():

    # Create a file to write
    filename = "image_gray.pgm"
    fi = open(filename,"w")

    # Header
    fi.write("P2\n")  # Grayscale image
    nb_col = 200
    nb_lin = 200
    fi.write(str(nb_col) + " " + str(nb_lin) + "\n")
    levels = 255
    fi.write(str(levels) + "\n")    

    for i in range(nb_lin):
        line = ""
        for j in range(nb_col):
            col = (i**2 + j**2) % 256   # a level of gray: a function of i and j
            line = line + str(col) + " "    
        line = line + "\n"

        # Write line
        fi.write(line)

    # Close file
    fi.close()

    return

# Test

print("--- File 'image_gray.pgm' ---")
write_image_gray()


## Question 3 ##

def ecrire_fichier_image_col():

    # Create a file to write
    filename = "image_col.ppm"
    fic = open(filename,"w")

    # Header
    fic.write("P3\n")  # Color image
    nb_col = 200
    nb_lin = 200
    fic.write(str(nb_col) + " " + str(nb_lin) + "\n")
    levels = 255
    fic.write(str(levels) + "\n")    

    for i in range(nb_lin):
        line = ""
        for j in range(nb_col):
            R = (i*j) % 256      # red level
            G = i % 256          # green level
            B = (i+j)//3 % 256   # blue level

            line = line + str(R) + " " + str(G) + " "  + str(B) + "   "  
        line = line + "\n"

        # Write line
        fic.write(line)

    # Close file
    fic.close()

    return

# Test

print("--- File 'image_col.ppm' ---")
ecrire_fichier_image_col()




## Question 4 ##

def inverse_black_white(filename):

    # Input file
    fi_in = open(filename,"r")

    # Output file
    name, extension = os.path.splitext(filename)
    new_name = name + "_inverse" + extension 
    fi_out = open(new_name,"w")


    i = 0    # Line number
    for line in fi_in:

        if i<2:     # Keep first 2 lines
            fi_out.write(line)  
        else:
            mylist = line.split()
            new_line = ""
            for l in mylist:
                if l == "1":
                    new_line = new_line + "0 "
                else:
                    new_line = new_line + "1 "

            new_line = new_line + "\n"
            fi_out.write(new_line)

        i = i + 1

    # Close all files
    fi_in.close()
    fi_out.close()
    return

print("--- Inverse black and white ---")
inverse_black_white("simple_bw.pbm")


## Question 4 ##

def formula_color_to_gray(R,G,B):
    gray = round(0.21*R + 0.72*G + 0.07*R)
    return gray

def color_to_gray(filename):

    # Input file
    fi_in = open(filename,"r")

    # Output
    name, extension = os.path.splitext(filename)
    new_name = name + "_gray" + ".pgm"
    fi_out = open(new_name,"w")


    i = 0    # Line number
    for line in fi_in:
        if i == 0:
            fi_out.write("P2\n")  # Grayscale image
        elif i == 1 or i == 2:    # Keep line 2 and 3
            fi_out.write(line)  
        else:
            mylist = line.split()
            new_line = ""

            j = 0  # Column number
            while j < len(mylist):
                R = int(mylist[j])
                G = int(mylist[j+1])
                B = int(mylist[j+2])
                gray = formula_color_to_gray(R,G,B)
                new_line = new_line + str(gray) + " "
                
                j = j + 3

            new_line = new_line + "\n"
            fi_out.write(new_line)

        i = i + 1

    # Close all files
    fi_in.close()
    fi_out.close()
    return

print("--- Color to grayscale ---")
color_to_gray("image_col.ppm")


