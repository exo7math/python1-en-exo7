
##############################
# If ... then ...
##############################

##############################
# Activity 1 - Quiz multiplications
##############################

from random import *

a = randint(1,10)
b = randint(1,10)

print("How much is the product",a,"times",b,"?")
answer_str = input("Your answer: ")
answer_int = int(answer_str) 

if answer_int == a*b:
    print("Well done!")
else:
    print("Lost! The correct answer was",a*b)


