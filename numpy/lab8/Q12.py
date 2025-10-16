import numpy as np


def matrix_multiply(a,b):
    return a.dot(b)  

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(matrix_multiply(a,b)) 
