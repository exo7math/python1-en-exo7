
##############################
# Lists I
##############################

##############################
# Lesson 1 - Construct a list

list_squares = []    # Start from the empty list

for i in range(10):
    list_squares.append(i**2)   # Add one square

print(list_squares)


##############################
# Lesson 2 - Plot a list

import matplotlib.pyplot as plt


mylist1 = [3,5,9,8,0,3]
mylist2 = [4,7,7,2,8,9]
plt.plot(mylist1,color="red")
plt.plot(mylist2,color="blue")
plt.grid()
plt.show()



list_x = [2, 3, 5, 7, 9]
list_y = [4, 9, 25, 49, 81]
plt.plot(list_x,list_y,color="red")
plt.grid()
plt.show()

