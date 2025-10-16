import pandas as pd

data = pd.read_csv('data.csv')

#random selection of the row using weights in a csv file
random_row = data.sample(weights=data['Period'], n=1)

print(random_row)