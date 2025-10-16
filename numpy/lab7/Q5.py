import numpy as np


arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

diag = [int(arr[i,i]) for i in range(4)]
print(diag)
