import numpy as np


def square1(x):
    n = len(x)
    result = np.zeros(n)
    for i in range(n):
        result[i] = x[i]**2
    return result


def square2(x):
    return x**2



def sum_arrays(a,b):
    return a+b

a = np.array([1,2,3])
b = np.array([4,5,6])       
print(square1(a))
print(square2(a))
print(sum_arrays(a,b))