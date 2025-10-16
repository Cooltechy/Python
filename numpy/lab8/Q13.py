import numpy as np


a = np.ones((6,6))
a[1:-1,1:-1] = 0
print(a)