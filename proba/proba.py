
##############################
# Probablities - Parrondo's paradox
##############################

# Reference : "Paradoxe de Parrondo", La gazette des mathématiciens, july 2017

from random import *


##############################
# Activity 1 - Game A : first losing game
##############################

## Question 1 ##
def throw_game_A():
    x = random()
    if x <= 0.49:
        return +1
    else:
        return -1


## Question 2 ##
def gain_game_A(N):
    gain = 0
    for i in range(N):
        gain = gain + throw_game_A()

    return gain


## Question 3 ##
def expected_value_game_A(N):
    expected_value = gain_game_A(N)/N
    return expected_value

# Test
print("--- Game A ---")
N = 1000000
print(expected_value_game_A(N))


##############################
# Activity 2 - Game B : second losing game 
##############################

## Question 1 ##
def throw_game_B(g):
    if g%3 == 0:
        x = random()
        if x <= 0.09:
            return +1
        else:
            return -1
    else:
        x = random()
        if x <= 0.74:
            return +1
        else:
            return -1


## Question 2 ##
def gain_game_B(N):
    gain = 0
    for i in range(N):
        gain = gain + throw_game_B(gain)

    return gain


## Question 3 ##
def expected_value_game_B(N):
    expected_value = gain_game_B(N)/N
    return expected_value

# Test
print("--- Game B ---")
N = 1000000
print(expected_value_game_B(N))


##############################
# Activity 3 -  Paradoxe de Parrondo
##############################

## Question 1 ##
def throw_game_AB(g):
    x = random()
    if x < 0.5:
        return throw_game_A()
    else:
        return throw_game_B(g)
    
    
## Question 2 ##
def gain_game_AB(N):
    gain = 0
    for i in range(N):
        gain = gain + throw_game_AB(gain)
    return gain


## Question 3 ##
def expected_value_game_AB(N):
    expected_value = gain_game_AB(N)/N
    return expected_value

# Test
print("--- Game AB ---")
N = 1000000
print(expected_value_game_AB(N))