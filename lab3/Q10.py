# input string where all occurrenc of first character is replaced with '$', except the first character

def replace_first_char(string):
    if not string:
        return string
    first_char = string[0]
    return first_char + string[1:].replace(first_char, '$')

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = replace_first_char(input_string)
    print("Modified string:", result)