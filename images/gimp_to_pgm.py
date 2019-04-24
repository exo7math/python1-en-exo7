
##############################
# Conversion of Gimp pgm format
# to our basic pgm format 
##############################

import os

def gimp_to_pgm(filename):

    # File to read
    fic_in = open("input/"+filename+".pgm","r")

    # File to write
    name, extension = os.path.splitext(filename)
    new_name = "input/"+name + "_new"+".pgm"
    fic_out = open(new_name,"w")


    i = 0  # Line number
    j = 0  # Column number
    
    new_line = ""
    
    for line in fic_in:
        if i == 0:
            fic_out.write("P2\n")   # Grayscale image

        elif i == 1:
            pass  
                              # Don't keep comments
        elif i == 2:          # Keep rpws/columns
            list_line = line.split()
            nb_col = int(list_line[0])
            nb_lig = int(list_line[1])
            fic_out.write(line)  

        elif i == 3:     # Keep levels
            fic_out.write(line)  

        else:
            line = line.split()[0]

            new_line = new_line + line + " "
                
            j = j + 1 

            if j == nb_col:
                new_line = new_line + "\n"
                fic_out.write(new_line)
                new_line = ""
                j = 0
        i = i + 1

    # Close files
    fic_in.close()
    fic_out.close()
    return

##################################

# gimp_to_pgm("pi_gimp")
# gimp_to_pgm("chat_gimp")
# gimp_to_pgm("reveil_gimp")
gimp_to_pgm("surf_gimp")