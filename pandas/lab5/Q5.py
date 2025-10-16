import pandas as pd
df = pd.DataFrame({'Age': [25, 30, 18, 45 , 66 , 88 ,11 , 32 , 15 , 18]})

def age_group(age):
    if age < 20:
        return 'Teen'
    elif age < 40:
        return 'Adult'
    else:
        return 'Senior'
df['Age_Group'] = df['Age'].map(age_group)

print(df)