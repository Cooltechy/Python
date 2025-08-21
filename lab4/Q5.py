#list of words and return the length of the longest word


words = input("Enter a list of words separated by commas: ").split(",")

length_longest_word = 0

for word in words:
    if len(word) > length_longest_word:
        length_longest_word = len(word)

print("Length of the longest word:", length_longest_word)
