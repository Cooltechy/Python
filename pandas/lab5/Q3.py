import pandas as pd


a = [x ** 2 for x in range(1, 11)]
b = [x ** 3 for x in range(1, 11)]

pdA = pd.Series(a, index=[f'Square of {i}' for i in range(1, 11)])
pdB = pd.Series(b, index=[f'Square of {i}' for i in range(1, 11)])

print(pdA+pdB)
# print(pdB)