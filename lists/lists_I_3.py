
##############################
# Lists I
##############################

##############################
# Activity 3 - Bubble sort
##############################

def bubble_sort(thelist):

    newlist = list(thelist)  
    
    n = len(newlist)

    for i in range(n-1,-1,-1):
        for j in range(i):
            if newlist[j+1] < newlist[j]:
                el = newlist[j]
                newlist[j] = newlist[j+1]
                newlist[j+1] = el

    return newlist

# Test
print("--- Bubble sort ---")
print(bubble_sort([13,11,7,4,6,8,12,6]))

thelist = [13,11,7,4,6,8,12,6]
newlist = bubble_sort(thelist)
print(thelist)
print(newlist)


print(sorted([13,11,7,4,6,8,12,6]))

thelist = [13,11,7,4,6,8,12,6]
thelist.sort()
print(thelist)
