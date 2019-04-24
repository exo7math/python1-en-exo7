# First function (not very clever)
def my_function_1(n):
    divis = False
    for k in range(n):
        if k*7 == n:
            divis = True
    return divis

# Second function (faster)
def my_function_2(n):
    if n % 7 == 0:
        return True
    else:
        return False

# Measurement of execution times
import timeit

print(timeit.timeit("my_function_1(1000)", 
    setup="from __main__ import my_function_1", 
    number=100000))
print(timeit.timeit("my_function_2(1000)", 
    setup="from __main__ import my_function_2", 
    number=100000))
