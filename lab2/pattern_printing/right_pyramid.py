# This program prints a right pyramid pattern of stars based on the user's input.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print()
for i in range(n-1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print()
