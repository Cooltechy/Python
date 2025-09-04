import pandas as pd
data1 = pd.read_csv('student.csv')
data2 = pd.read_csv('data.csv')

#merge two different csv file having diff column names
merged_data = pd.concat([data1, data2], axis=0, ignore_index=True)


print(merged_data)