import numpy as np

#convert one data type to another datatype 
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
arr = arr.astype(str)


print(arr)