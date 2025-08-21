#Add 'ing' at the end of a given string. If it's already ending with 'ing', add 'ly' instead.


string = input("Enter a string: ")
if string.endswith("ing"):
    string += "ly"
else:
    string += "ing"
print("Modified string:", string)