import pandas as pd

data = pd.read_csv('data.csv')

data = data.select_dtypes(include=['number'])

# print(data.info())

print(data.describe())

# print(data['Period'].mean())
# print(data['Period'].min())


