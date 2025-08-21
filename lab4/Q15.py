# a perform union, intersection and difference 
# b find common elements between two list 

list1 = eval(input("Enter first list: "))
list2 = eval(input("Enter second list: "))

common_elements = []
for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

union_list = list(set(list1) | set(list2))
intersection_list = list(set(list1) & set(list2))
difference_list = list(set(list1) - set(list2))

print("Common elements between the two lists:", common_elements)
print("Union of the two lists:", union_list)
print("Intersection of the two lists:", intersection_list)
print("Difference of the two lists:", difference_list)