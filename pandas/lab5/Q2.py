import pandas as pd
    
data = [x**3 for x in range(1 , 11)]

pdData = pd.Series(data , index = [f'Cube of {i}' for i in range(1, 11)])

print(pdData)

print(pdData['Cube of 9'])