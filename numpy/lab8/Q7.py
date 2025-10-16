import numpy as np


a = np.arange(25).reshape(5,5)
print(a)


print(a[:3,:3])
print(a[:3,2:])
print(a[2:,2:])
print(a[2:,:3])
print(a[2:,2:])