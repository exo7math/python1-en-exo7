
##############################
# If ... then ... 
##############################

##############################
# Activity 5 - The Mytery number
##############################


##############################
## Question 1 ##

from random import *

# Classic mystery number

mystery_nb = randint(0,99)

for trial in range(7):
    print("What is the mystery number?")
    answer_str = input("Your proposal:")
    answer_int = int(answer_str) 
    if mystery_nb == answer_int:
        print("Bravo!")
        break # Stop the loop

    if mystery_nb < answer_int:
        print("No, the number to find is smaller!")   

    if mystery_nb > answer_int:
        print("No, the number to find is bigger!")

# When it's over:
if mystery_nb != answer_int:
    print("Lost! The mystery number was",mystery_nb)


##############################
## Question 2 ##

# Variant: the computer lies (1 time out of 4)

# mystery_nb = randint(0,99)

# for trial in range(7):
#     print("What's the mystery number?")
#     answer_str = input("Your proposal:")
#     answer_int = int(answer_str) 

#     # # 1 time out of 4 (about) the computer lies
#     tell_truth = True
#     chance = randint(1,4)
#     if chance == 4:
#         tell_truth = False 

#     if mystery_nb == answer_int:
#         print("Bravo!")
#         break # Stop the loop
    
#     if mystery_nb < answer_int:
#         if tell_truth == True:
#             print("No, the number to find is smaller!")    
#         else:
#             print("No, the number to find is bigger!")   

#     if mystery_nb > answer_int:
#         if tell_truth == True:
#             print("No, the number to find is bigger!")
#         else: 
#             print("No, the number to find is smaller!")

# # When it's over:
# if mystery_nb != answer_int:
#     print("Lost! The mystery number was",mystery_nb)


##############################
## Question 3 ##

# Variant: the mystery number changes a little

# mystery_nb = randint(0,99)
# print(mystery_nb)
# for trial in range(7):
#     print("What's the mystery number?")
#     answer_str = input("Your proposal:")
#     answer_int = int(answer_str) 

#     # Modification of the mystery number
#     chance = randint(-3,3)
#     mystery_nb = mystery_nb + chance
#     if mystery_nb < 1:
#         mystery_nb = 1
#     if mystery_nb > 99:
#         mystery_nb = 99

#     if mystery_nb == answer_int:
#         print("Bravo!")
#         break # Stop the loop
    
#     if mystery_nb < answer_int:
#         print("No, the number to find is smaller!")   

#     if mystery_nb > answer_int:
#         print("No, the number to find is bigger!")

# # When it's over:
# if mystery_nb != answer_int:
#     print("Lost! The mystery number was",mystery_nb)

