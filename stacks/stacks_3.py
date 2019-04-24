
##############################
# Stacks - Polish calculator
##############################


##############################
# From activity 1
##############################

def push_to_stack(element):
    global stack
    stack = stack + [element]
    return None

def pop_from_stack():
    global stack
    top = stack[len(stack)-1]
    stack = stack[0:len(stack)-1]
    return top   

def is_stack_empty():
    if len(stack) == 0:
        return True
    else:
        return False

##############################
# Activity 3 - La gare de triage
##############################


def sort_wagons(train):
    """ Sort red/blue wagons of a train
    Input: a train with blue wagons (numbers) and red ones (letters)
    Output: the wagons sorted with blue before, then red
    Action: use a stack """
    
    global stack   # Should be global to be modified
    stack = []

    new_train = ""

    for wagon in train.split():
        if wagon.isdigit():   # Blue wagin directly to output station
            new_train = new_train + wagon + " "
        else:                 # Red wagon in waiting area
            push_to_stack(wagon)

    # Now all blue wagons are well placed
    # We deal with the red ones
    while not is_stack_empty():
        wagon = pop_from_stack()
        new_train = new_train + wagon + " "

    return new_train


# Tests
print("--- Red/blue sort ---")

train = "A 4 C 12"
sorted_train = sort_wagons(train)
print(train,' -> ',sorted_train)

train = "9 K 8 P 17 L B R 3 10 2 N"
sorted_train = sort_wagons(train)
print(train,' -> ',sorted_train)