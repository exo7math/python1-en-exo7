
##############################
# Dynamic images
##############################

import os   # for images files


##############################
# Activity 1 - Photo booth
##############################



##############################
## From other chpater ##
def print_array(array):
    
    n = len(array)
    m = len(array[0])

    for i in range(n):
        for j in range(m):
            print('{:>3d}'.format(array[i][j])," ", end="")
        print()

    return


##############################
## Question 1 ##

def transformation(i,j,n):
    if i%2 == 0 and j%2 == 0:
        ii = i//2
        jj = j//2
    if i%2 == 0 and j%2 == 1:
        ii = i//2
        jj = (n+j)//2    
    if i%2 == 1 and j%2 == 0:
        ii = (n+i)//2
        jj = j//2
    if i%2 == 1 and j%2 == 1:
        ii = (n+i)//2
        jj = (n+j)//2    

    return ii,jj

## Test ##
print("--- Photo booth transformation ---")
print(transformation(1,1,6))


##############################
## Question 2 ##

def photo_booth(array):
    n = len(array)
    new_array = [[0 for j in range(n)] for i in range(n)]   

    for i in range(n):
        for j in range(n):
            ii, jj = transformation(i,j,n)
            new_array[ii][jj] = array[i][j]

    return new_array

## Test ##
print("--- Transformation photo_booth ---")
array_before = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16] ]
array_after = photo_booth(array_before)
print_array(array_before)
print("---")
print_array(array_after)


##############################
## Question 3 ##
def photo_booth_iterate(array,k):
    n = len(array)
    tab = [[array[i][j] for j in range(n)] for i in range(n)]

    for i in range(k):
        tab = photo_booth(tab)

    return tab


## Test ##
print("--- Iterate transformation photo_booth ---")
array = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16] ]
print_array(array)
for k in range(1,10):
    array_iter = photo_booth_iterate(array,k)
    # Not very clever because start from the begining each time
    print("--- k =",k,"---")
    print_array(array_iter)



##############################
# Activity 2 - Conversion array/image
##############################


##############################
## Question 1 ##
def array_to_image(array,image_name):

    # New file to write
    filename = "output/" + image_name + ".pgm"
    fi = open(filename,"w")

    # Header
    fi.write("P2\n")  # Grayscale image

    nb_lin = len(array)
    nb_col = len(array[0])

    fi.write(str(nb_col) + " " + str(nb_lin) + "\n")
    levels = 255
    fi.write(str(levels) + "\n")    

    for i in range(nb_lin):
        line = ""
        for j in range(nb_col):
            color = array[i][j]
            line = line + str(color) + " "    
        line = line + "\n"

        # WWrite line to file
        fi.write(line)

    # Clos file
    fi.close()

    return


## Test ##
print("--- Array to image ---")
array =  [[128, 192, 128, 192, 128], [224, 0, 228, 0, 224], [228, 228, 228, 228, 228], [224, 64, 64, 64, 224], [192, 192, 192, 192, 192]]
array_to_image(array,"test")  


##############################
## Question 2 ##

def image_to_array(image_name):

    # New file to write
    filename = "input/" + image_name + ".pgm"
    fi = open(filename,"r")

    i = 0    # Line number
    for line in fi:
        if i == 1:     # Keep first 2 lines
            list_line = line.split()
            nb_col = int(list_line[0])
            nb_lin = int(list_line[1])

            array = [[ 0 for j in range(nb_col)] for i in range(nb_lin)]
        elif i > 2:
            mylist = line.split()
            for j in range(nb_col):
                array[i-3][j] = int(mylist[j])

        i = i + 1

    # Close file
    fi.close()

    return array

print("--- Image to array ---")

test_array = image_to_array("test") 
print(test_array)
print_array(test_array)


##############################
## From chapter "Files" ##
## Provide examples of file to test with

def write_file_gray_image():

    # New file to write
    filenmae = "input/image_gray.pgm"
    fi = open(filenmae,"w")

    # Header
    fi.write("P2\n")  # Grayscale image
    nb_col = 256
    nb_lin = 256
    fi.write(str(nb_col) + " " + str(nb_lin) + "\n")
    levels = 255
    fi.write(str(levels) + "\n")    

    for i in range(nb_lin):
        line = ""
        for j in range(nb_col):
            color = (i**2 + j**2) % 256   # one gray level, a function of i and j
            line = line + str(color) + " "    
        line = line + "\n"

        # Write line to file
        fi.write(line)

    # Close file
    fi.close()

    return

# Test

print("--- File 'image.pgm' ---")
# write_file_gray_image()


##############################
# Activity 1bis - Photo booth
##############################

##############################
## Question 4 ##

def photo_booth_images(image_name,kmax):
    array = image_to_array(image_name)
    array_to_image(array,image_name+"_photo_"+str(0)) # initial image

    n = len(array)
    tab = [[array[i][j] for j in range(n)] for i in range(n)]

    for k in range(1,kmax+1):
        tab = photo_booth(tab)
        array_to_image(tab,image_name+"_photo_"+str(k))

    return

## Test ##
photo_booth_images("image_gray",8)
# photo_booth_images("pi_gimp_new",8)
# photo_booth_images("cat_gimp_new",8)



##############################
# Activity 3 - Baker's transfomation
##############################

##############################
## Question 1 ##

def baker_stretch(array):
    n = len(array)
    new_array = [[0 for j in range(2*n)] for i in range(n//2)]   

    for i in range(n//2):
        for j in range(2*n):
            if j%2 == 0:
                new_array[i][j] = array[2*i][j//2]
            else:
                new_array[i][j] = array[2*i+1][j//2]

    return new_array


print("--- Baker : stretch an array ---")
array = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16] ]
array_stretch = baker_stretch(array)
print_array(array)
print("---")
print_array(array_stretch)


##############################
## Question 2 ##

def baker_fold(array):
    n = 2*len(array)

    new_array = [[0 for j in range(n)] for i in range(n)]  

    # top part
    for i in range(n//2):
        for j in range(n):
            new_array[i][j] = array[i][j]

     # bottom part
    for i in range(n//2,n):
        for j in range(n):
            new_array[i][j] = array[n//2 - i - 1][2*n-1-j]             

    # for i in range(n//2):
    #     for j in range(n):
    #         new_array[n-i-1][j] = array[i][2*n-1-j]  
    

    return new_array    

print("--- Baker : fold array ---")
array_fold = baker_fold(array_stretch)
print_array(array_stretch)
print("---")
print_array(array_fold)


##############################
## Question 3 ##

def baker_iterate(array,k):
    n = len(array)
    tab = [[array[i][j] for j in range(n)] for i in range(n)]

    for i in range(k):
        tabb = baker_stretch(tab)
        tab = baker_fold(tabb)

    return tab


print("--- Boulanger : iterate tranformation array ---")
array = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16] ]
print_array(array)
for k in range(1,10):
    array_iter = baker_iterate(array,k)
    print("--- k =",k,"---")
    print_array(array_iter)

 

##############################
## Question 4 ##

def baker_images(image_name,kmax):

    array = image_to_array(image_name)
    array_to_image(array,image_name+"_baker_"+str(0)) # image init

    n = len(array)
    tab = [[array[i][j] for j in range(n)] for i in range(n)]

    for k in range(1,kmax+1):
        tabb = baker_stretch(tab)
        tab = baker_fold(tabb)
        array_to_image(tab,image_name+"_baker_"+str(k))

    return

## Test ## 
baker_images("image_gray",17)
# baker_images("pi_gimp_new",17)
# baker_images("cat_gimp_new",17)
# baker_images("clock_gimp_new",17)
# baker_images("surf_gimp_new",15)
