import pandas as pd
import numpy as np

df = pd.read_csv('student.csv')

df = df[df.isnull().any(axis=1)]

print(df)



print('*****************************')


df['name'] = df['name'].fillna('33333333')


df['class'] = df['class'].fillna(np.random.choice(['Four', 'Five', 'Six', 'Seven', 'Nine', 'Ten']))

df['mark'] = df['mark'].fillna(np.random.randint(50, 101))


df['gender'] = df['gender'].fillna(np.random.choice(['male', 'female']))

print(df)