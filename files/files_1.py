
##############################
# Files
##############################

from random import *


##############################
# Activity 1 - Write to a file
##############################

## Question 1 ##

def write_file_grades():

    # Creation of a file to write
    filename = "grades.txt"
    fi = open(filename,"w")

    # Lists names
    list_firstnames = ["Lara","Robin","Hermione","Bill","Alice","James","Tintin"]
    list_names = ["Skywalker","Croft","Voldemort","Vador","Bond","Parker"]

    for i in range(6):
        firstname = choice(list_firstnames)
        name = choice(list_names)
        grade = str(randint(10,40)/2) + " " + str(randint(10,40)/2) + " " + str(randint(10,40)/2)
        line = firstname + " " + name + " " + grade + "\n"

        # Write line
        fi.write(line)

    # Close file
    fi.close()

    return

# Test

print("--- File 'grades.txt' ---")
write_file_grades()


## Question 2 ##

def write_file_averages():

    # File to read
    file_grades = "grades.txt"
    fi_in = open(file_grades,"r")

    # File to write
    file_averages = "averages.txt"
    fi_out = open(file_averages,"w")

    for line in fi_in:
        mylist = line.split()
        average = (float(mylist[2])+float(mylist[3])+float(mylist[4]))/3
        average_str = '{0:.2f}'.format(average)
        new_line = mylist[0] + " " + mylist[1] + " " + average_str + "\n"
        fi_out.write(new_line)

    # Fermeture des fichiers
    fi_in.close()
    fi_out.close()
    return

print("--- File 'averages.txt' ---")
write_file_averages()




