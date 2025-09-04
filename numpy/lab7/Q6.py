import numpy as np


arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])


anti_diag = [int(arr[i,-i-1]) for i in range(4)]
print(anti_diag)