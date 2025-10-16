import pandas as pd

data = pd.read_csv('student.csv')

# Find and print all duplicate rows (excluding the first occurrence)
duplicate_rows = data[data.duplicated()]
print("Duplicate rows:")
print(duplicate_rows)

print('***************************************************')

data.drop_duplicates(inplace=True)

print("Data after removing duplicates:")
print(data)