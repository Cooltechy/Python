# input from user and perform merge of two tuples and remove duplicates

tup1 = eval(input("Enter first tuple: "))
tup2 = eval(input("Enter second tuple: "))

merged_tup = tup1 + tup2
unique_tup = tuple(set(merged_tup))
print("Merged tuple without duplicates:", unique_tup)


