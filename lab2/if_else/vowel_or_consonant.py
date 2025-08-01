# This program takes a single character input from the user and determines if it is a vowel, consonant, or not a letter.

Char = input("Enter a character: ")
if Char.isalpha():
    if Char.lower() in 'aeiou':
        print(f"'{Char}' is a vowel.")
    else:
        print(f"'{Char}' is a consonant.")
else:
    print(f"'{Char}' is not a letter.")
