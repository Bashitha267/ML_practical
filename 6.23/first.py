import pandas as pd
df=pd.read_csv('student_data.csv')
print("Display few rows:")
print(df.head())
print('Colomn Names',df.info())
print('rows and columns',df.shape)
