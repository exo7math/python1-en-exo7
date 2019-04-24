
##############################
# Files
##############################

##############################
# Write in a file
##############################

# Creation of a file to write
fi = open("my_file.txt","w")

# Write first line
fi.write("Hello world!\n")

# Write second line
line = "Hi there.\n"
fi.write(line)

fi.close()

##############################
# Read lines from a file
##############################

fi = open("my_file.txt","r")

for line in fi:
    print(line)

fi.close()