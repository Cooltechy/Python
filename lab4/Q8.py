# sentence as a input and creates a dict each key is a word from sentence and each value is the number of character in that word


def word_length_dict(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    result = word_length_dict(user_input)
    print("Word length dictionary:", result)
