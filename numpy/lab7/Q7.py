import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])


print("Using view")

y = arr.view()

y[1,1] = 42
print(y)
print(arr)


print()
print("Using copy() method")

x = arr.copy()

x[3,3] = 99

print(x)
print(arr)