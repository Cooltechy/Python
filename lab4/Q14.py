# checking if one tuple is subset of another
tup1 = eval(input("Enter first tuple: "))
tup2 = eval(input("Enter second tuple: "))

is_subset = True
for item in tup1:
    if item not in tup2:
        is_subset = False
        break

if is_subset:
    print("Tuple 1 is a subset of Tuple 2")
else:
    print("Tuple 1 is not a subset of Tuple 2")
