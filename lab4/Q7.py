#taking input from user rotate a tuple n positions to the right without converting into list

tup = eval(input("Enter a tuple (e.g., (1, 2, 3)): "))
n = int(input("Enter the number of positions to rotate: "))

if n < 0 or n >= len(tup):
    print("Invalid number of positions to rotate.")
else:
    rotated_tup = tup[-n:] + tup[:-n]
    print("Rotated tuple:", rotated_tup)
