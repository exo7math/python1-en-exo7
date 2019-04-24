
##############################
# Bitcoin
##############################



from random import randint
from time import *



##############################
# Activity 2 - Tools for lists
##############################

# Global constant for length of blockks
N = 6

# Constant for proof of work
Max = [0,0,25]


##############################

## Question 1 ##

# Addition of terms of two lists of the same size (and modulo 100)
def addition(mylist1,mylist2):
    list_sum = []
    for i in range(len(mylist1)):
        list_sum = list_sum + [ (mylist1[i]+mylist2[i]) % 100 ]

    return list_sum
    
# Test
print("--- Test list sum ---")   
print(addition([1,2,3,4,5,6],[1,1,1,1,1,1]))


##############################

## Question 2 ##

# Test if a list is small than max_list
def is_smaller(mylist,max_list):
    i = 0
    n = len(max_list)
    while (i < n) and (mylist[i] <= max_list[i]):
        i = i + 1
    if i == n:
        return True
    else:
        return False
    
# Test
print("--- Test list small ---")   
print(is_smaller([0,0,24,4,5,6],[0,0,50]))


##############################

## Question 3 ##

def sentence_to_list(sentence):
    # Transform letters to numbers less than 100
    mylist = [ord(c) % 100 for c in sentence]

    # Rajoute des 0 devant si besoin
    while len(mylist) % N > 0:
        mylist = [0] + mylist

    return mylist

# Test
print("--- Sentence to list ---")
sentence = "Be happy!" 
print(sentence)
print(sentence_to_list(sentence))  



##############################
# Activity 3 - Hasch function
##############################



##############################

## Question 3 ##
p = [7,11,13,17,19,23] # prime numbers

def one_round(block):
    # Addition
    block[1] = (block[1]+block[0]) % 100
    block[3] = (block[3]+block[2]) % 100
    block[5] = (block[5]+block[4]) % 100

    # m = p*m + 1 (modulo 100)
    for i in range(N):
        block[i] = (p[i]*block[i]+1) %  100
    # permutation
    block = [block[N-1]] + block[:N-1]
    return block

# Test
print("--- Test one round ---")
block = [0,1,2,3,4,5]
print(block)
print(one_round(block))

block = [1,1,2,3,4,5]
print(block)
print(one_round(block))


##############################

## Question 3 ##

def ten_rounds(block):
    for i in range(10):
        block = one_round(block)
    return block

# Test
print("--- Test ten rounds ---")
block = [0,1,2,3,4,5]
print(block)
print(ten_rounds(block))

block = [1,1,2,3,4,5]
print(block)
print(ten_rounds(block))

block = [99,96,87,56,67,76]
print(block)
print(ten_rounds(block))

block = [70,92,22,4,16,90]
print(block)
print(ten_rounds(block))


##############################

## Question 3 ##
def bithash(mylist):

    while len(mylist)>N:
        block1 = mylist[0:N]  # First block
        block2 = mylist[N:2*N] # Second block
        end_list = mylist[2*N:] # Remaining blocks
        # print(block1)
        # print(block2)
        # print(end_list)

        #block1 = one_round(block1)   # One round
        block1 = ten_rounds(block1) # Ten rounds

        #print(block1)

        new_block_begin = addition(block1,block2)

        mylist = new_block_begin + end_list

    # Lasr ten rounds for mylist (that only contain one block)
    # mylist = one_round(mylist) # One round
    mylist = ten_rounds(mylist) # Ten rounds

    return mylist

# Test
print("--- Hash of a list ---")

mylist = [1,2,3,4,5,6,1,2,3,4,5,6]
thehash = bithash(mylist)
print(mylist)
print(thehash)

mylist = [1,1,3,4,5,6,1,2,3,4,5,6]
thehash = bithash(mylist)
print(mylist)
print(thehash)


mylist = [0,1,2,3,4,5,1,1,1,1,1,1,10,10,10,10,10,10]
thehash = bithash(mylist)
print(mylist)
print(thehash)



##############################


##############################
# Activity 4 - Proof of work - Minage
##############################

##############################

## Question 3 ##

def verification_proof_of_work(mylist,proof):

    list_test = mylist + proof
    thehash = bithash(list_test)
    # print(proof,thehash)
    if is_smaller(thehash,Max):
        return True
    else:
        return False

# Test
print("--- Verif Proof of work ---")    

mylist = [0,1,2,3,4,5]
proof = [12, 3, 24, 72, 47, 77]
# Max = [0,0,7]

start_time = time()
print(verification_proof_of_work(mylist,proof))
end_time = time()
duration = end_time-start_time

print("Time of computation:",duration)

##############################

## Question 2 ##

def proof_of_work(mylist):

    thehash = [1,1,1,1,1,1]

    while not(is_smaller(thehash,Max)): 
        proof = [randint(0,99) for i in range(N)]
        list_test = mylist + proof
        thehash = bithash(list_test)
    print(proof,thehash)

    return proof

##############################

## Question 2 bis ##

from itertools import product

def proof_of_work_bis(mylist):
    for proof in product(range(100),range(100),range(100),range(100),range(100),range(100)):
        proof = list(proof)
        list_test = mylist + proof
        thehash = bithash(list_test)
        if is_smaller(thehash,Max):
            break

    print(proof,thehash)
    return proof
    
##############################

## Question 3 ##

# Test
print("--- Proof of work ---")    

start_time = time()
mylist = [0,1,2,3,4,5]
# proof = proof_of_work(mylist)
# proof = proof_of_work_bis(mylist)
end_time = time()
duration = end_time-start_time

print("Time of computation:",duration)


##############################
# Activity 5 - Tes bitcoins
##############################

##############################

## Question 1 ##

proof_init = [0,0,0,0,0,0]   # random values
blockchain = [proof_init]

def add_transaction(transaction):
    global blockchain
    blockchain = blockchain + [transaction]
    return blockchain

# Test
print("--- Initialization of the register book and first transaction ---")
print(blockchain)
add_transaction("Bob +135")
print(blockchain)


##############################

## Question 2 ##

def mining():
    global blockchain
    transaction = blockchain[-1]
    prev_proof = blockchain[-2]
    # print(transaction)
    # print(prev_thehash)
    # print(sentence_to_list(transaction))
    mylist = prev_proof + sentence_to_list(transaction)

    proof = proof_of_work(mylist)

    blockchain = blockchain + [proof]

    return blockchain

# Test
print("--- Mining  ---")
print(blockchain)
mining()
print(blockchain)

print("--- Example for chapter  ---")
Max = [0,0,7]
thehash_init = [3,1,4,1,5,9]   # random values
blockchain = [thehash_init]
add_transaction("Abel +35")
print(blockchain)
mining()
print(blockchain)

##############################

## Question 3 ##

def verification_blockchain():
    prev_proof = blockchain[-3]        
    transaction = blockchain[-2]
    proof = blockchain[-1]
    thehash = bithash(prev_proof+sentence_to_list(transaction)+proof)
    if is_smaller(thehash,Max):
        return True
    else:
        return False


# Test
print("--- Verification of the blockchain  ---")
print(blockchain)
print(verification_blockchain())



##############################

## Question 4 ##
# Full example

# Constant for proof of work
Max = [0,0,7]


start_time = time()  # start chrono

thehash_init = [0,0,0,0,0,0]   # random values
blockchain = [thehash_init]

print(blockchain)
add_transaction("Abel +135")
print(blockchain)
mining()
print(blockchain)
print(verification_blockchain())

add_transaction("Bob -77")
print(blockchain)
mining()
print(blockchain)
print(verification_blockchain())

add_transaction("Camille -25")
print(blockchain)
mining()
print(blockchain)
print(verification_blockchain())

end_time = time()
duration = end_time-start_time
print("Time of computation:",duration)