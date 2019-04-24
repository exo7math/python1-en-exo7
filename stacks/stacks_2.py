
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
# Activity 2 - Stack manipulation
##############################

## Question 1 ##

print("--- Manipulation ---")
stack = []
push_to_stack(5)
push_to_stack(7)
push_to_stack(2)
push_to_stack(4)
print(stack)
pop_from_stack()
push_to_stack(8)
push_to_stack(1)
push_to_stack(3)
print(stack)
val =  pop_from_stack()
print('Value:',val)

## Question 2 ##

def is_in_stack(element):
    """  Test if the stack contains the element
    Input: nothing
    Output: true/false
    Action: modify the stack """
    
    while not is_stack_empty():
        el = pop_from_stack()
        if el == element:
            return True    # If found element it's ok

    return False     # End without finding element


# Tests
print("--- Test if stack contains 7 ---")

# Test 1
stack = [4,5,6]
print(stack,'stack contains 7?',is_in_stack(7))

# Test 2
stack = [4,7,12,99]
print(stack,'stack contains 7?',is_in_stack(7))


## Question 3 ##

def sum_stack():
    """ Compute the sum of the stack
    Input: nothing
    Output: the sum
    Action: the stack is now empty """
    
    mysum = 0
    while not is_stack_empty():
        element = pop_from_stack()
        mysum = mysum + element

    return mysum


# Test
print("--- Sum of the values of the stack ---")
stack = [4,5,6]
print('The sum of',stack,'is',sum_stack())


## Question 4 ##

def penultimate():
    """ Return the second last element at the bottom of the stack
    Input: nothing
    Output: the penultimate (=second last) element
    Action: the stack is now empty """
    
    last = None
    penultimate = None  

    while not is_stack_empty():
        penultimate = last         # The last become the second last
        last = pop_from_stack()    # New last
    
    return penultimate


# Tests
stack = [4,5,6,13]
print('The second last element of',stack,'is',penultimate())

stack = [4,6]
print('The second last element of',stack,'is',penultimate())

stack = [6]
print('The second last element of',stack,'is',penultimate())

stack = []
print('The second last element of',stack,'is',penultimate())

