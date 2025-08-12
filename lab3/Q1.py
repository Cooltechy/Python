#program to count freq of each word in a line of text
line = input("Enter a line of text: ")
words = line.split()            
word_count = {}
for word in words:  
    word = word.lower()  # Convert to lowercase for case-insensitive counting
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word count
print("Word count:")
for word, count in word_count.items():
    print(f"{word}: {count}")   
          