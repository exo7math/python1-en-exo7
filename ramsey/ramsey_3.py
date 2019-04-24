
##############################
# Ramsey graphs and combinatorics
##############################


##############################
# Activity 3 - Binary
##############################


def integer_to_binary(p,n):
    str_b = bin(p)  # Conversion to binary notation
    str_bb = str_b[2:]  # We cut off the prefix
    # Transformation to a list of **intgers** 0 or 1
    list_binary = []
    for b in str_bb:
        list_binary = list_binary + [int(b)]

    # Add zeros at the begining if necessary
    nb_zeros = n - len(list_binary)
    for i in range(nb_zeros):
        list_binary = [0] + list_binary

    return list_binary


# Short version, using "format()"
def integer_to_binary_bis(p,n):
    model = '{:0'+str(n)+'b}'
    str_binary = model.format(p)
    list_binary = [int(b) for b in list(str_binary)]
    return list_binary


# Test 
if __name__ == '__main__':
    n = 8
    p = 37
    print(integer_to_binary(p,n))
    print(integer_to_binary_bis(p,n))








