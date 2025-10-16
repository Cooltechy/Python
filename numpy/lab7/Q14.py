import numpy as np


a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([
    [9, 8, 7], 
    [6, 5, 4],
    [3, 2, 1]
])

print("stacked")
stacked = np.stack((a, b))
print(stacked)




print("stacking row wise")
row_stacked = np.stack((a, b), axis=1)
print(row_stacked)
print()


print("stacking column wise")
col_stacked = np.stack((a, b), axis=2)
print(col_stacked)
print()

