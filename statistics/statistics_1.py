
##############################
# Statistics -- Data visualization -- tkinter
##############################


##############################
# Activity 1 - Statistics
##############################

from math import *

##################################################
## Question 1 ##

def mysum(mylist):
    """ Compute the um of elements
    Input: a list of numbers
    Output: their sum """    

    S = 0
    for x in mylist:
        S = S + x
    return S


# Test 
print("--- Sum ---")
mylist = [5,18,6,3]
print(mylist)
print(mysum(mylist))
print(sum(mylist))


##################################################
## Question 2 ##

def mean(mylist):
    """ Compute the average of the items of the list
    Input: a list of numbers
    Output: the average """    
    
    nblist = len(mylist)

    if nblist == 0:
        M = 0
    else:
        M = mysum(mylist) / nblist 

    return M


# Test 
print("--- Mean ---")
mylist = [5,18,6,3]
print(mylist)
print(mean(mylist))



##################################################
## Question 3 ##

def minimum(mylist):
    """ Return the minimum among the elements
    Input: a list of numbers
    Output: their minimum """    
    
    if len(mylist) == 0:
        return None

    mini = mylist[0]
    for i in range(1,len(mylist)):
        if mylist[i] < mini:
            mini = mylist[i]

    return mini


# Test 
print("--- Minimum ---")
mylist = [6,8,2,10]
print(mylist)
print(minimum(mylist))
print(min(mylist))


##################################################
def maximum(mylist):
    """ Return the maximum among the elements
    Input: a list of numbers
    Output: their maximum """     
    
    if len(mylist) == 0:
        return None

    maxi = mylist[0]
    for i in range(1,len(mylist)):
        if mylist[i] > maxi:
            maxi = mylist[i]

    return maxi


# Test 
print("--- Maximum ---")
mylist = [6,8,2,10]
print(mylist)
print(maximum(mylist))
print(max(mylist))



##################################################
## Question 4 ##

def variance(mylist):
    """ Return the variance of the elements
    Input: a list of numbers
    Output: their variance """      

    if len(mylist) == 0:
        return 0
 
    M = mean(mylist)

    sum_square = 0
    for x in mylist:
        sum_square = sum_square + (x-M)**2
    
    var = sum_square / len(mylist)

    return var


# Test 
print("--- Variance ---")
mylist = [6,8,2,10]
print(mylist)
print(variance(mylist))


##################################################
## Question 5 ##

def standard_deviation(mylist):
    """ Return the standard deviation of the elements
    Input: a list of numbers
    Output: their standard deviation """    

    eca = sqrt(variance(mylist))

    return eca


# Test 
print("--- Ecart-type ---")
mylist = [6,8,2,10]
print(mylist)
print(standard_deviation(mylist))


##################################################
## Question 6 ##

temp_london = [4.9,5,7.2,9.7,13.1,16.6,18.7,18.2,15.5,11.6,7.7,5.6 ]

temp_chicago = [-5 ,-2.7,2.8,9.2,15.2,20.7,23.5,22.6,18.4,12.1,4.8,-1.9]

#temp_brest = [6.4,6.5,8.5,9.7,11.9,14.6,15.9,16.3,15.1,12.2,9.2,7.1]
#temp_strasbourg = [0.9,2.4,6.1,9.7,13.8,17.2,19.2,18.6,15.7,10.7,5.3,2.1]


print(mean(temp_london))
print(mean(temp_chicago))
print(standard_deviation(temp_london))
print(standard_deviation(temp_chicago))

