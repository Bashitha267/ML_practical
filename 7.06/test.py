import pandas as pd
import numpy as np
df=pd.read_csv('student_data.csv')

df.drop_duplicates(inplace=True)
print("before format")
print(df)

df['Gender']=df['Gender'].str.lower().str.strip()
gender_map={'male':'Male','female':'Female','f':'Female','m':'Male'}
df['Gender']=df['Gender'].map(gender_map)
print("Formatted")
print(df)
df['Age']=pd.to_numeric(df['Age'],errors='coerce')
print(df['Age'])
df['Age']=df['Age'].fillna(df['Age'].median())
print("Filling the NA with median")
print(df['Age'])   
df['Age']=df['Age'].fillna(df['Age'].mode())
print("Filling the NA with mode")
print(df['Age'])   

df['Department']=df['Department'].replace('Computer Since','Computer Science')
print(df)
print("Noisy data cleaned.")
print(df)
upper_limit=60000
lower_limit=30000

df['Salary']=np.where(
    df['Salary']>upper_limit,
    upper_limit,
    np.where(
        df['Salary']<lower_limit,lower_limit,df['Salary']
    )

)
print(df)