# create a single string seperated with space from two strings by swapping the characters at the position 1

def swap_first_char(string1, string2):
    if not string1 or not string2:
        return string1 + " " + string2
    # Swap the first character of both strings
    swapped_string = string1[0] + string2[1] + string1[2:] + " " + string2[0] + string1[1] + string2[2:]
    return swapped_string
    

if __name__ == "__main__":  
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    
    result = swap_first_char(string1, string2)
    print("Resulting string:", result)