import numpy as np

def euclidean_distance(a,b):
    return np.sqrt(np.sum((a-b)**2))

a = np.array([1,2,3])
b = np.array([4,5,6])


print(euclidean_distance(a,b))