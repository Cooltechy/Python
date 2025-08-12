# program to prompt the user to enter two lists of integers. 
# a. Whether the list are of the same length
# b. Whether the list sums to same value
# c. Whether any value occurs in both lists

def same_length(list1, list2):
    return len(list1) == len(list2) 

def same_sum(list1, list2):
    return sum(list1) == sum(list2) 

def common_values(list1, list2):
    return any(value in list2 for value in list1)

if __name__ == "__main__":
    list1_input = input("Enter first list of integers separated by spaces: ")
    list1 = [int(num) for num in list1_input.split()]
    
    list2_input = input("Enter second list of integers separated by spaces: ")
    list2 = [int(num) for num in list2_input.split()]

    print("Same length:", same_length(list1, list2))
    print("Same sum:", same_sum(list1, list2))
    print("Common values:", common_values(list1, list2))

