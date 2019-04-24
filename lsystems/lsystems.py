
##############################
# L-systems
##############################

from turtle import *


##############################
# Activity 1 - Draw a L-system
##############################


def draw_lsystem(word,angle=90,scale=1):

    speed("fastest")
    width(2)
    color('blue')
    up()
    goto(-150,0)
    down()

    for c in word:
        if c == "A" or c == "B":
            forward(100*scale)
        if c == "l":
            left(angle)
        if c == "r":
            right(angle) 

    exitonclick()

    return

## Test ##
# draw_lsystem("AlArAArArA")


##############################
# Activity 2 - Only one rule: Koch snowflake
##############################

# A L-system
# One starting word
# One rule of find-and-repalce

##################################################
## Question 1 ##

def replace_1(word,letter,pattern):
    new_word = ""
    for c in word:
        if c == letter:
            new_word = new_word + pattern
        else:
            new_word = new_word + c

    return new_word

## Test ##
print("--- Replace one letter ---")
word = "ArAAl"
new_word = replace_1(word,"A","Al")
print(word)
print(new_word)




##################################################
## Question 2 ##

def iterate_lsysteme_1(start,rule,k):
    word = start
    letter = rule[0]
    pattern = rule[1]

    for i in range(k):
        word = replace_1(word,letter,pattern)

    return word


print("--- Lesson 1: Replace one letter and iterat ---")
word = "BlArB"
rule = ("A","ABA")
for k in range(4):
    new_word = iterate_lsysteme_1(word,rule,k)
    print(new_word)


##################################################
## Question 3 ##

## Koch snowflake
start_Koch = "A"
rule_Koch = ("A","AlArArAlA")

## Test
print("--- Koch's snowflake ---")
for k in range(4):
    print(k,iterate_lsysteme_1(start_Koch,rule_Koch,k))

k = 3
word = iterate_lsysteme_1(start_Koch,rule_Koch,k)
# draw_lsystem(word,scale=5/3**k)


##################################################
## Question 4 ##

#####################
## Other examples ##

#####################
start = "ArArArA"
rule = ("A","ArAlAlAArArAlA")
k = 3
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem(word,scale=0.05)

#####################
start = "ArArArA"
rule = ("A","AlAArAArArAlAlAArArAlAlAAlAArA")
k = 2
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem(word,scale=0.07)

#####################
start = "ArArArA"
rule = ("A","AArArArArAA")
k = 3
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem(word,scale=0.1)

#####################
start = "ArArArA"
rule = ("A","AArArrArA")
k = 3
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem(word,scale=0.1)

#####################
start = "ArArArA"
rule = ("A","AArArArArArAlA")

k = 3
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem(word,scale=0.1)
#####################
start = "ArArArA"
rule = ("A","AArAlArArAA")
k = 3
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem(word,scale=0.15)

#####################
start = "ArArArA"
rule = ("A","ArAArrArA")
k = 3
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem(word,scale=0.15)

#####################
start = "ArArArA"
rule = ("A","ArAlArArA")
k = 4
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem(word,scale=0.15)



##############################
# Activity 3 - Two rules: Sierpinski's triangle
##############################

##################################################
## Question 1 ##

def replace_2(word,letter1,pattern1,letter2,pattern2):
    new_word = ""
    for c in word:
        if c == letter1:
            new_word = new_word + pattern1
        elif c == letter2:
            new_word = new_word + pattern2
        else:
            new_word = new_word + c

    return new_word

## Test ##
print("--- Replace two letters ---")
word = "ArBlA"
new_word = replace_2(word,"A","ABl","B","Br")
print(word)
print("Good:",new_word)

word1 = replace_1(word,"A","ABl")
word2 = replace_1(word1,"B","Br")
print("Bad:",word2)

##################################################
## Question 2 ##

def iterate_lsysteme_2(start,rule1,rule2,k):
    word = start
    letter1 = rule1[0]
    pattern1 = rule1[1]
    letter2 = rule2[0]
    pattern2 = rule2[1]

    for i in range(k):
        word = replace_2(word,letter1,pattern1,letter2,pattern2)
    return word

print("--- Lesson 1: Replace two letter and iterate ---")
word = "A"
rule1 = ("A","BlA")
rule2 = ("B","BB")

for k in range(4):
    new_word = iterate_lsysteme_2(word,rule1,rule2,k)
    print(new_word)

##################################################
## Question 3 ##

## Triangle de Sierpinski
start_Sierp = "ArBrB"
rule_Sierp_1 = ("A","ArBlAlBrA")
rule_Sierp_2 = ("B","BB")

## Test
print("--- Sierpinski ---")
for k in range(3):
    print(k,iterate_lsysteme_2(start_Sierp,rule_Sierp_1,rule_Sierp_2,k))

k = 4
word = iterate_lsysteme_2(start_Sierp,rule_Sierp_1,rule_Sierp_2,k)
# draw_lsystem(word,angle=-120,scale=5/2**k)

##################################################
## Question 4 ##

#####################
## Other examples ##

#####################
## Dragon's curve
start_dragon = "AX"
rule_dragon_1 = ("X","XlYAl")
rule_dragon_2 = ("Y","rAXrY")

k = 9
word = iterate_lsysteme_2(start_dragon,rule_dragon_1,rule_dragon_2,k)
# draw_lsystem(word,scale=2/k)

#####################
## Variant Sierpinski (angle = 60)
start = "A"
rule1 = ("A","BrArB")
rule2 = ("B","AlBlA")
# angle = 60

k = 5
word = iterate_lsysteme_2(start,rule1,rule2,k)
# draw_lsystem(word,angle=60,scale=2/k**2)


#####################
## Gosper's curve
start = "A"
rule1 = ("A","AlBllBrArrAArBl")
rule2 = ("B","rAlBBllBlArrArB")
k = 3
word = iterate_lsysteme_2(start,rule1,rule2,k)
# draw_lsystem(word,angle=60,scale=2/k**2)


##############################
# Activity 4 - Draw a L-system with a stack
##############################


##################################################
## Question 1 ##

def draw_lsystem_stack(word,angle=90,scale=1):

    speed("fastest")
    width(3)
    color('blue')
    up()
    goto(0,-300)
    down()

    stack = []

    for c in word:
        if c == "A" or c == "B":
            forward(100*scale)
        if c == "a":
            up()
            forward(100*scale)
            down()
        if c == "l":
            left(angle)
        if c == "r":
            right(angle)
        if c == "[":
            stack = stack + [(position(),heading())]
        if c == "]":
            up()
            pos,direc = stack.pop()
            goto(pos)
            setheading(direc)
            down()

    exitonclick()

    return

## Test
# draw_lsystem_stack("AaAlAA[lAAA][rAA]A",angle=90,scale=1)
# draw_lsystem_stack("AlA[lAAA]A[rAA]A",angle=90,scale=1)

##################################################
## Question 2 ##

# Plant
start_plant = "lllX"
rule_plant_1 = ("X","A[lX][X]A[lX]rAX")
rule_plant_2 = ("A","AA")


k = 5
word = iterate_lsysteme_2(start_plant,rule_plant_1,rule_plant_2,k)
# draw_lsystem_stack(word,angle=30,scale=1/k**(3/2))



#####################
## Example with up-down ##
start = "ArArArA"
rule1 = ("A","AlarAAlAlAAlAalAAralAArArAArAarAAA")
rule2 = ("a","aaaaaa")
k = 2
word = iterate_lsysteme_2(start,rule1,rule2,k)
draw_lsystem_stack(word,scale=0.1)


#####################
## Other examples of plants ##

# #####################
# angle = 22.5
start = "lllA"
rule = ("A","A[lA]A[rA][A]")
k = 4
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem_stack(word,angle=30,scale=0.2)


# #####################
# angle = 30
start = "lllA"
rule = ("A","A[lA]A[rA]A")
k = 4
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem_stack(word,angle=30,scale=0.075)

# ####################
# angle = 22.5
start = "lllA"
rule = ("A","AAr[rAlAlA]l[lArArA]")
k = 3
word = iterate_lsysteme_1(start,rule,k)
# draw_lsystem_stack(word,angle=30,scale=0.2)


# #####################
# angle = 25.7
start = "lllX"
rule1 = ("X","A[lX]A[rX]AX")
rule2 = ("A","AA")
k = 5
word = iterate_lsysteme_2(start,rule1,rule2,k)
# draw_lsystem_stack(word,angle=30,scale=0.07)

# #####################
# angle = 25.7
start = "lllX"
rule1 = ("X","A[lX][X]A[lX]rAX")
rule2 = ("A","AA")
k = 5
word = iterate_lsysteme_2(start,rule1,rule2,k)
# draw_lsystem_stack(word,angle=30,scale=0.07)

# #####################
# angle = 30
start = "lllA"
rule1 = ("A","A[rB][lB]")
rule2 = ("B","A[rB]A[lArB]")
k = 5
word = iterate_lsysteme_2(start,rule1,rule2,k)
# draw_lsystem_stack(word,angle=30,scale=0.25)

#####################
# angle = 30
start = "lllX"
rule1 = ("X","Ar[[X]lX]lA[lAX]rX")
rule2 = ("A","AA")
k = 4
word = iterate_lsysteme_2(start,rule1,rule2,k)
# draw_lsystem_stack(word,angle=30,scale=0.15)




#####################
#####################
# Hilbert curve
# For the illustration of each part of the book
  # \rule{L -> +RF-LFL-FR+}
  # \rule{R -> -LF+RFR+FL-}}
# angle = 30
start = "X"
rule1 = ("X","lYArXAXrAYl")
rule2 = ("Y","rXAlYAYlAXr")
k = 4
word = iterate_lsysteme_2(start,rule1,rule2,k)
draw_lsystem_stack(word,angle=90,scale=0.15)