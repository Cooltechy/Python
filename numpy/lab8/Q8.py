import numpy as np


a = np.array([[1, 2], [3, 4]])
mean = np.mean(a, axis=0)
centered_a = a - mean
print(centered_a)   
print(centered_a.mean(axis=0)) 