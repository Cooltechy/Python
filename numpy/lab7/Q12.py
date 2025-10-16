import numpy as np

arr = np.array([
    [7, 8, 9],
    [22, 11, 2],
    [1, 2, 3],
    [4, 5, 6]
])


arr = arr[arr[:, 1].argsort()]

print(arr)