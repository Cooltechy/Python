##program to exchange first and last characters of a string
def exchange_first_last(input_string):
    if len(input_string) < 2:
        return input_string  # No exchange needed for strings with less than 2 characters
    return input_string[-1] + input_string[1:-1] + input_string[0] 

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    output_string = exchange_first_last(input_string)
    print("String after exchanging first and last characters:", output_string)

