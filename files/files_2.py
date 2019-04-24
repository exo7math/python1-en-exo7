
##############################
# Files
##############################

from random import *
import matplotlib.pyplot as plt

##############################
# Activity 2 - 
##############################

## Question 1 ##

def write_file_sales():

    # Create a file to write
    filename = "sales.csv"
    fi = open(filename,"w")

    # List of products nom
    list_products = ["Mountain bike","Surfboard","Running shoes","Badminton racket","Volley ball"]

    # Top lines
    fi.write("Best sales of the brand 'Pentathlon'\n\n")
    fi.write(",2015,2016,2017,2018,2019,2020\n\n")

    for product in list_products:
        
        # Generate random sales
        sales = ""
        for i in range(6):
            sales = sales + "," + str(randint(50,100)*10)

        line = product + sales  + "\n" 

        # Write
        fi.write(line)

    # Close file
    fi.close()

    return

print("--- Files 'sales.csv' ---")
write_file_sales()


## Question 2 ##

def display_sales():

    # File to read
    file_sales = "sales.csv"
    fi_in = open(file_sales,"r")

    num_line = 0
    for line in fi_in:
        if num_line > 3: # we forget the top lines
            mylist = line.split(",")
            data = [float(x) for x in mylist[1:]]
            plt.plot(data)

        num_line += 1

    # Close file
    fi_in.close()

    # Display
    plt.grid()
    plt.show()

    return

print("--- Display 'sales.csv' ---")
display_sales()

