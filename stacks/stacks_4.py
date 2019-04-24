
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
# Activity 4 - Polish calculator
##############################

## Question 1 ##

def operation(a,b,op):
    """ Compute the operation 'a + b 'ou 'a * b'...
    Input: a,b (numbers) and 'op' a character '+'' ou '*'
    Output: the result of the computation """
    
    if op == '+':
        return a + b
    if op == '*':
        return a * b


# Tests
print("--- Operations ---")
a=5 ; b=7
print("The sum of ",a,"and",b,"is",operation(a,b,'+'))
print("The product of",a,"and",b,"is",operation(a,b,'*'))


## Question 2 ##

def polish_calculator(expression):
    """ Evaluate an expression given in Polish notation
    Input: a Polish expression 
    Output: the result of the computation
    Action: use a stack """
    
    global stack
    stack = []

    list_expression = expression.split()

    for charac in list_expression:
        if (charac == '+') or (charac == '*'):
            b = pop_from_stack()
            a = pop_from_stack()
            partial_result = operation(a,b,charac)
            push_to_stack(partial_result)
        else:
            val = int(charac)
            push_to_stack(val)

    return pop_from_stack()


# Tests
print("--- Polish calculator ---")

exp = "2 3 +"
print("The result of the expression",exp,"is",polish_calculator(exp))

exp = "2 3 + 5 *"
print("The result of the expression",exp,"is",polish_calculator(exp))

exp = "8 7 3 + *"
print("The result of the expression",exp,"is",polish_calculator(exp))

exp = "8 7 3 * +"
print("The result of the expression",exp,"is",polish_calculator(exp))