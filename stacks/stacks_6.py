
##############################
# Stacks - Polish calculator
##############################

global stack

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
# From activity 4
##############################

def operation(a,b,op):  
    if op == '+':
        return a + b
    if op == '*':
        return a * b

       
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



##############################
# Activity 6 - Conversion to Polish notation
##############################

def polish_notation(expression):
    """ Convert a classic expression to Polish notation
    Input: a classic expression
    Output: its Polish notation
    Action: use a stack """
    
    global stack
    stack = []

    list_expression = expression.split()

    polish = ""    # For the Polsih notation

    for charac in list_expression:
        if charac.isdigit():
            polish = polish + charac + " "

        if charac == "(":
            push_to_stack(charac)

        if charac == "*":
            push_to_stack(charac)

        if charac == "+":
            while not is_stack_empty():
                element = pop_from_stack()                
                if element == "*":
                    polish = polish + element + " "            
                else:
                    push_to_stack(element)    # Put back the element
                    break
            push_to_stack(charac)            

        if charac == ")":
            while not is_stack_empty():
                element = pop_from_stack()                
                if element == "(":
                    break
                else:
                    polish = polish + element + " "

    while not is_stack_empty():
        element = pop_from_stack()                
        polish = polish + element + " "    

    return polish

# Tests
print("--- Conversion to Polish notation ---")

exp = "2 + 3"
print("The expression",exp,"is written",polish_notation(exp))

exp = "2 * 3"
print("The expression",exp,"is written",polish_notation(exp))

exp = "( 2 + 3 ) * 4"
print("The expression",exp,"is written",polish_notation(exp))

exp = "4 * ( 2 + 3 )"
print("The expression",exp,"is written",polish_notation(exp))

exp = "2 + 4 * 5"
print("The expression",exp,"is written",polish_notation(exp))

exp = "2 * 4 * 5"
print("The expression",exp,"is written",polish_notation(exp))

exp = "( 2 + 3 ) * ( 4 + 8 )"
print("The expression",exp,"is written",polish_notation(exp))


##
# Automatic test and verifiacations

def test_polish(expression):
    classic = eval(expression)
    print("---\n",classic)
    conversion = polish_notation(expression)
    print(conversion)
    polish = polish_calculator(conversion)
    print(polish)
    return classic == polish


exp = "2 + 3"
print(exp, "OK ?",test_polish(exp))

exp = "2 * 3 * 7"
print(exp, "OK ?",test_polish(exp))
 
exp = "( 2 + 3 ) * ( 4 + 8 )"
print(exp, "OK ?",test_polish(exp))

exp = "( ( 2 + 3 ) * 11 ) * ( 4 + ( 8 + 5 ) )"
print(exp, "OK ?",test_polish(exp))

exp = "( 17 * ( 2 + 3 ) ) + ( 4 + ( 8 * 5 ) )"
print(exp, "OK ?",test_polish(exp))