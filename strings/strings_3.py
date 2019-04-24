
##############################
# Strings - Text analysis 
##############################


##############################
# Activity 3 - DNA sequences
##############################

## Question 1 ##

def presence_of_A(sequence):
    """ Determine if the there is a nucleotid  A
    Input: a sequence of A,C,T,G (a string)
    Output: true or false """

    for nucleotid in sequence:
        if nucleotid == 'A':
            return True

    return False


# Test 
sequence = "AGACAGCGAGCATATGCAGGAAG"
answer = presence_of_A(sequence)
print("Is there a 'A'  in the sequence",sequence," : ",answer)


## Question 2 ##

def position_of_AT(sequence):
    """ Determine the position of the code AT
    Input: a sequence of A,C,T,G (a string)
    Output: the position of this subsequence (start at 0) """   

    for i in range(len(sequence)-1):
        if sequence[i] == 'A' and sequence[i+1] == 'T':
            return i  # If found

    return None  # If nowhere found
    

# Test 
sequence = "GTGGTTTGACCTCCCATGGCCAT"
pos = position_of_AT(sequence)
print("In the sequence",sequence,"the code AT appears in position",pos)

    
## Question 3 ##

def position(code,sequence):
    """ Determine the position of the code in the given sequence
    Input: a code and a sequence of A,C,T,G (two strings)
    Output: the position of this code (start at 0) """  
       
    for i in range(len(sequence)-len(code)):
        if code == sequence[i:i+len(code)]:
            return i  # If found, it's over

    return None  # If nowhere found
  

# Test 
sequence = "GAAGACCTTCTCCTCCTGC"
code = "CCTC"
pos = position(code,sequence)
print("In the sequence",sequence,"the code',code,'appears in position",pos)


## Question 4 ##


def investigation():
    mustard = "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
    scarlet = "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
    peacock = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
    plum    = "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"

    code1 = "CATA"
    code2 = "ATGC"

    for suspect in [mustard,scarlet,peacock,plum]:
        print(position(code1,suspect))
        print(position(code2,suspect))

    return


# Investigation
print("--- Investigation ---")
investigation()

