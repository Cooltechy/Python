# count frequency of characters in a string

string = input("Enter a string: ")
char_frequency = {}
for char in string:
    char_frequency[char] = char_frequency.get(char, 0) + 1
print("Character frequency in the string:", char_frequency)