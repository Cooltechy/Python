import pandas as pd

data = pd.read_csv('student.csv')
df1  = pd.DataFrame(data)


data2 = pd.read_csv('student.csv')
df2  = pd.DataFrame(data2)


df_diff = df1.compare(df2)
print("Element-wise difference:")
print(df_diff)
    

df_side_by_side = pd.concat([df1, df2], axis=1, keys=['DF1', 'DF2'])
print("Side by side difference:")
print(df_side_by_side)


if df1.equals(df2):
    print("DataFrames are identical")
else:
    print("DataFrames are not identical")
