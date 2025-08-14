import streamlit as st

'Learning Streamlit'

import pandas as pd

# df = pd.DataFrame({'Name' : ['Masala Chai', 'Green Tea', 'Black Tea', 'Herbal Tea'],
#                    'Price' : [50, 30, 40, 60]
#                  })

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })

st.write(df)



