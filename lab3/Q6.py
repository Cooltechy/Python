#List comprehension 
# a. generate positive list of numbers from a given list
# b. square of N numbers
# c. list of vowels in a given word
# d. list of ordinal values of characters in a given word

def positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def square_numbers(numbers):
    return [num ** 2 for num in numbers]    

def vowels_in_word(word):
    vowels = "aeiouAEIOU"
    return [char for char in word if char in vowels]   

def ordinal_values(word):
    return [ord(char) for char in word]     



if __name__ == "__main__":  
    
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [int(num) for num in numbers_input.split()]
    
    word = input("Enter a word or sentence: ")

    print("Positive numbers:", positive_numbers(numbers))
    print("Square of numbers:", square_numbers(numbers))
    print("Vowels in word:", vowels_in_word(word))
    print("Ordinal values of characters:", ordinal_values(word))
