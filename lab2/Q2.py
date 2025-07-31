Char = input("Enter a character: ")
if Char.isalpha():
    if Char.lower() in 'aeiou':
        print(f"'{Char}' is a vowel.")
    else:
        print(f"'{Char}' is a consonant.")
else:
    print(f"'{Char}' is not a letter.")
