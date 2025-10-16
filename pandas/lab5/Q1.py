import pandas as pd

data = pd.read_csv('student.csv')


print('**********************   Information   **********************')
print(data.info())

print()
print('**********************   First 5 records of csv file   **********************')
print(data.head())

print()
print('**********************   Last 5 records of csv file   **********************')
print(data.tail())

row_names_list = data.index.tolist()
print(row_names_list)