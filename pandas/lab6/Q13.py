import pandas as pd
data = pd.read_csv('data.csv')

# sort data using column
sorted_data = data.sort_values(by='Period', ascending=True)

print(sorted_data)