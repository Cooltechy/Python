# a. multiply all values of dict
# b. add all values of dict
# c. concatenate two dict in one

def concatenate_dicts(dict1, dict2):
    return {**dict1, **dict2}

def multiply_dict_values(input_dict):
    result = 1
    for value in input_dict.values():
        result *= value
    return result

def add_dict_values(input_dict):
    return sum(input_dict.values())

if __name__ == "__main__":
    while True:
        choice = int(input("Choose an operation (1. multiply\n2. add\n3. concatenate)\n4. Exit "))
        match choice:
            case 1:
                dic = eval(input("Enter dictionary: "))
                print("Product of values:", multiply_dict_values(dic))
            case 2:
                dic = eval(input("Enter dictionary: "))
                print("Sum of values:", add_dict_values(dic))
            case 3:
                dic1 = eval(input("Enter first dictionary: "))
                dic2 = eval(input("Enter second dictionary: "))
                print("Concatenated dictionary:", concatenate_dicts(dic1, dic2))
            case 4:
                break
            case _:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
