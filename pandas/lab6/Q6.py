import pandas as pd

data = pd.read_csv('student.csv')

for index, row in data.iterrows():
    print(row)

for col in data.columns:
    print(data[col])