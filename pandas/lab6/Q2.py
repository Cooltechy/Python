import pandas as pd

data = pd.read_csv('data.csv')

data = data.select_dtypes(include=['number'])

print(data.corr())