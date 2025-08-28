import pandas as pd

data = pd.read_csv('student.csv')

df = pd.DataFrame(data)


df = df.drop('gender' , axis=1)

print(df)