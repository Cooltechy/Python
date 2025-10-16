import numpy as np

mat = np.array([
    [111, 232, 33, 4],
    [55, 6, 47, 8],
    [39, 10, 111, 112],
])


#replace minimum value in each row by #
for i in range(mat.shape[0]):
    mat[i, mat[i].argmin()] = -100

print(mat)