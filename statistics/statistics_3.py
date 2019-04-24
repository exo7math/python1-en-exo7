##############################
# Statistics -- Data visualization -- tkinter
##############################


##############################
# Activity 3 - Statistics (bis)
##############################


##################################################
## Question 1 ##

from math import *
from random import *

def median(mylist):
    """ Compute the median of the elements
    Input: a list of numbers
    Output: their median """        
    my_sorted_list = sorted(mylist)

    n = len(my_sorted_list)

    if n%2 == 0:   # n est pair
        rank_middle = n//2
        med = (my_sorted_list[rank_middle-1]+my_sorted_list[rank_middle]) / 2
    else: 
        rank_middle = (n-1)//2 
        med = my_sorted_list[rank_middle]

    return med


# Test 
print("--- Médiane ---")
mylist = [5,18,6,3]
print(mylist)
print(median(mylist))



##################################################
## Question 2 ##

def grades_to_list(grade_count):
    """ Takes a number of gradess as input and returns the list of grades 
    Input: a list that counts each grade
    Output: the list of all grades """        
    mylist = []
    for i in range(len(grade_count)):
        nb = grade_count[i]
        mylist = mylist + [i]*nb

    return mylist


# Test 
print("--- List from a grade count ---")
grade_count = [0,0,1,2,5,2,3,5,4,1,2]
# grade_count = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
# grade_count = [randint(1,5) for i in range(21)]
print(grade_count)
print(grades_to_list(grade_count))

def median_grades(grade_count):
    """ Calcule la médiane des grades
    Input : une mylist d'effectif de grades
    Output : la médiane """   
    mylist = grades_to_list(grade_count)
    med = median(mylist)

    return med


# Test 
print("--- Médiane des grades ---")
# grade_count = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
grade_count = [0,0,1,2,5,2,3,5,4,1,2]
print(grade_count)
print(median_grades(grade_count))



##################################################
## Question 3 ##

def quartiles(mylist):
    """ Compute tes quartiles of the list
    Input: a list of numbers
    Output: their three quartiles Q1, Q2=median, Q3 """        
    med = median(mylist)

    my_sorted_list = sorted(mylist)
    n = len(my_sorted_list)
    rank_middle = n//2
    if n%2 == 0: # si n pair
        mylist_inf = mylist[:rank_middle]
        mylist_sup = mylist[rank_middle:]
    else: # n impair
        mylist_inf = mylist[:rank_middle+1]
        mylist_sup = mylist[rank_middle:]    
    Q1 =  median(mylist_inf)
    Q3 =  median(mylist_sup)

    return Q1, med, Q3


# Test 
print("--- Quartiles ---")
mylist = [3,4,5,7,12,50,100]
print(mylist)
print(quartiles(mylist))


##################################################
def quartiles_grades(grade_count):
    """ Compute the quartiles of the grades
    Input: a list of grade count
    Output: the quartiles """   
    mylist = grades_to_list(grade_count)
    Q1,Q2,Q3 = quartiles(mylist)

    return Q1, Q2, Q3


# Test 
print("--- Quartiles of the grades ---")
grade_count = [0,0,1,2,5,2,3,5,4,1,2]
print(grade_count)
print(quartiles_grades(grade_count))