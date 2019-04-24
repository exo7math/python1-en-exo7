
##############################
# Statistics -- Data visualization -- tkinter
##############################


##############################
# Activity 5 - Data visualization (bis)
##############################


##################################################
## Question 1 ##

from random import *

def index_stock_exchange(n):
    """ Simulate n days of market """
    val = 1000
    list_val = [val]
    for i in range(n-1):
        val = val + randint(-10,12)/3
        list_val = list_val + [val]

    return list_val


# Test
print(index_stock_exchange(100)) 


##################################################
## Question 2 ##

def graphic_point(mylist):
    """ Display the curve of the indices of the stock exchange """
    
    # Base 1000 at y = 300
    canvas.create_line(100,300,100+365,300,width=3)

    # Vertical axis on the left
    canvas.create_line(95,420,95,80)   
    for j in range(-1,3):
        canvas.create_line(90,300-100*j,95,300-100*j)
        canvas.create_text(72,300-100*j,text=str(1000+j*100))  

    # One point per day
    for i in range(len(mylist)):  
        canvas.create_rectangle(100+i,300+1000-mylist[i],100+i+1,300+1000-mylist[i],outline="red")

    return


# tkinter window
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Test
mylist = index_stock_exchange(365)
#graphic_point(mylist)
#root.mainloop()


##################################################
## Question 3 ##

def moving_average(mylist,duration):
    """ Compute the moving average """
    mov_av = []
    for i in range(len(mylist)-duration+1):
        moy = sum(mylist[i:i+duration])/duration
        mov_av = mov_av + [moy]

    return mov_av


# Test
mylist = [1,2,3,4,5,6]
print(mylist)
print(moving_average(mylist,2))


####################################################
## Question 4 ##

def graphic_moving_average(mylist):
    """ Display the moving averages at 7 and 30 days """
    # average 7 last days
    average_7 = moving_average(mylist,7) 
    for i in range(len(average_7)):  
        canvas.create_rectangle(100+i+6,300+1000-average_7[i],100+i+6+1,300+1000-average_7[i],outline="blue")

    # average 30 last days
    average_30 = moving_average(mylist,30)   
    for i in range(len(average_30)):  
        canvas.create_rectangle(100+i+29,300+1000-average_30[i],100+i+29+1,300+1000-average_30[i],outline="sienna")

    return


# Test
mylist = index_stock_exchange(365)
graphic_point(mylist)           # The index of the stock exchange
graphic_moving_average(mylist)  # The moving average at 7 and 30 days
root.mainloop()