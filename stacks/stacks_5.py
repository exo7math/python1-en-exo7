
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
# Activity 5 - Brackets well balanced
##############################

## Question 1 ##

def are_parentheses_balanced(expression):
    """ Test if an expression has correct parentheses
    Input: an expression (a string)
    Output: true/false
    Action: use a stack """
    
    global stack
    stack = []    # Start froman empty stack

    for charac in expression:
        if charac == "(":
            push_to_stack(charac)

        if charac == ")":
            if is_stack_empty():
                return False     # Problem: one "(" is missing 
            else:
                pop_from_stack()

    # At the end:
    if is_stack_empty():
        return True
    else: 
        return False


# Test
print("--- Well balanced parentheses ---")

expression = "(a+b)^2 = a^2 + (b^2+2(ab))"
print("The expression",expression,"has its parentheses correct?",are_parentheses_balanced(expression))

expression = "((a+b)^3 = (a+b)"
print("The expression",expression,"has its parentheses correct?",are_parentheses_balanced(expression))

expression = "(a+b)^4) = ((a+b)"
print("The expression",expression,"has its parentheses correct?",are_parentheses_balanced(expression))


## Question 2 ##

def are_brackets_balanced(expression):
    """ Test if an expression has correct square brackets and parentheses
    Input: an expression (a string)
    Output: true/false
    Action: use a stack """   
    
    global stack
    stack = []    # Start from an empty stack

    for charac in expression:
        if charac == "(" or charac == "[":
            push_to_stack(charac)

        if charac == ")" or charac == "]":
            if is_stack_empty():
                return False     # Problem: one "(" or "[" is missing
            else:
                element = pop_from_stack()
                if element == "[" and charac == ")":
                    return False     # Problem of type [)
                if element == "(" and charac == "]":
                    return False     # Problem of type (]

    # Zt the end
    return is_stack_empty()


# Test
print("--- Expression with correct square brackets and parentheses ---")

expression = "(a+b)^2 = (a^2 + [b^2+[2(ab)]])"
print("The expression",expression,"has its parentheses and square brackets correct?",are_brackets_balanced(expression))

expression = "((a+b)]^3 = [a+b]"
print("The expression",expression,"has its parentheses and square brackets correct?",are_brackets_balanced(expression))

expression = "[a+b)^4] = (a+b)"
print("The expression",expression,"has its parentheses and square brackets correct?",are_brackets_balanced(expression))

