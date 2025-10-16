import pandas as pd

data = pd.read_csv('data.csv')

data = data.select_dtypes(include=['number'])

#perform aggregate function
data_agg = data.agg(['mean' , 'sum'])

print(data_agg)