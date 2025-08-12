# accept a string and display the string after removing all the vowels
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in input_string if char not in vowels)
    return result
    
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    output_string = remove_vowels(input_string)
    print("String after removing vowels:", output_string)   