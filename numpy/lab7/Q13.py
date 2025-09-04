import numpy as np

mat = np.array([
    [111, 232, 33, 4],
    [55, 6, 47, 8],
    [39, 10, 111, 112],
])


for arr in mat:
    print(arr.max())