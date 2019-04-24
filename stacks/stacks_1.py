
##############################
# Stacks - Polish calculator
##############################


##############################
# Activity 1 - Operations on the stack
##############################


# "stack" is a global variable

## Question 1 ##

def push_to_stack(element):
    """  Add an element at the top of the stack
    Input: an object
    Output: nothing
    Action: the stack contains one more element """

    global stack     # In order to modify the stack

    stack = stack + [element]

    return None


# Test
print("--- Push ---")
stack = [4,5,6]
print('Stack before:',stack)
push_to_stack(7)
print('Stack after:',stack)


## Question 2 ##

def pop_from_stack():
    """ Read the element at the top of stack et remove it
    Input: nothing
    Output: the element at the top
    Action:  the stack contains one element less """

    global stack

    top = stack[len(stack)-1]
    stack = stack[0:len(stack)-1]

    return top


# Test
print("--- Pop ---")
stack = [4,5,6]
print('Stack before:',stack)
val = pop_from_stack()
print('Popped value:',val,'\nStack after:',stack)


## Question 3 ##

def is_stack_empty():
    """ Test if the stack is empty or not
    Input: nothing
    Output: true/false
    Action: doesn't modify the stack """

    if len(stack) == 0:
        return True
    else:
        return False


# Tests
print("--- Test if stack empty ---")

# Test 1
stack = [4,5,6]
empty = is_stack_empty()
print(stack,'stack empty?',empty)

# Test 2
stack = []
empty = is_stack_empty()
print(stack,'stack empty?',empty)

