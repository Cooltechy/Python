#program to prompt the user for a list of integers . For all values greater than 100, store 'over' instead of the value.

def replace_over_hundred(numbers):
    return ['over' if num > 100 else num for num in numbers]    

if __name__ == "__main__":
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(num) for num in numbers_input.split()]
    
    print("Processed list:", replace_over_hundred(numbers)) 

    