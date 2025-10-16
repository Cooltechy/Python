import numpy as np




print("1D array")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

for val in arr:
    print(val,end=" ")
print()




print("2D array")
arr_2d = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
])
for row in arr_2d:
    for val in row:
        print(val, end=" ")
    print()


print("3D array")
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])

for matrix in arr_3d:
    for row in matrix:
        for val in row:
            print(val, end=" ")
    print()
