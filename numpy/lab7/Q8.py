import numpy as np

arr = np.array([
    [1, 2, 3],
    [10,54,32],
    [7, 8, 9]
])

print("transpose")
transpose = arr.T
print(transpose)

print()



print("determinant" , end=" ")
det = np.linalg.det(arr)
print(det)



print("inverse")
inv = np.linalg.inv(arr)
print(inv)


print("flatten")
flatten = arr.flatten()
print(flatten)


