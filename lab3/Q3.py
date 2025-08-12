# program to find whether a character is present in a string if yes the print it's index
def find_character_index(input_string, character):
    index = input_string.find(character)
    if index != -1:
        return f"Character '{character}' found at index {index}."
    else:
        return f"Character '{character}' not found in the string."      

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    character = input("Enter a character to find its index: ")
    result = find_character_index(input_string, character)
    print(result)
