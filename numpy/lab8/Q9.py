import numpy as np


a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.sum(a, axis=0))  # column wise sum
print(np.sum(a, axis=1))  # row wise sum

print(np.max(a, axis=0))  # column wise max
print(np.max(a, axis=1))  # row wise max