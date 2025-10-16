import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


k = 3
top_k = arr[np.argpartition(-arr, k)[:k]]
print(top_k)