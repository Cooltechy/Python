#creating dataframe from a dictionary

import pandas as pd

dataAsDict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(dataAsDict)

print(df)
