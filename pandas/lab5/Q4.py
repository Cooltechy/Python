import pandas as pd

data = pd.read_csv('student.csv')

df = pd.DataFrame(data)

# df.index = ['Student'+str(i) for i in range(1, len(df)+1)]

# print(df)
df = df[df['gender'] != 'female']

print(df)

