import pandas as pd

df = pd.read_csv('./student_data.csv')
print("Display Few Data : ")
print(df.head()) # you can see few data from the dataset and not the whole dataset

print()

print('Discription: ', df.describe()) 
print('Number of rows and columns: ', df.shape)

print()

# 1. Removing Duplicates
df = df.drop_duplicates(subset = ['Student_ID'], keep = 'first')
print("Dupicates Removed!")
print(df)

print()

# 2. Fix Inconcictence in the data
df['Gender'] = df['Gender'].str.lower().str.strip()
gender_map = {'male': 'Male' , 'female':'Female','f':'Female','m':'Male'}
df['Gender'] = df['Gender'].map(gender_map)
print("Formatting standardized.")
print(df)

print()

# 3. Fix incorrect Data Types
df['Age'] = pd.to_numeric(df['Age'], errors = 'coerce')

print()

# Convert to numeric and coerce - if converion fails. force to mark the value as missing (NaN).

import numpy as np
df['Department'] = df['Department'].replace('0', np.nan)
print("Data types Corrected!")
print(df)

print()

# 4.Fill Missing Values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
# fillna - "Fill missing values." It replace NaN with another value.
# mode()[0] - first mode value
print("Missing values handled")
print(df)

print()

# 5. Handle Noisy Data
df['Department'] = df['Department'].replace('Computer Since','Computer Science')
print("Noisy data cleaned.")
print(df)

print()

# Define the salary limit
upper_limit = 60000
lower_limit = 30000

print()

# cap salary values
df['Salary'] = np.where(
	df['Salary'] > upper_limit,
	upper_limit,
	np.where(
	df['Salary'] < lower_limit,
	lower_limit,
	df['Salary'])
)
print(df)

print()

# Define the Age limit
upper_limit = 45
lower_limit = 24

print()

# cap Age values
df['Age'] = np.where(
	df['Age'] > upper_limit,
	upper_limit,
	np.where(
	df['Age'] < lower_limit,
	lower_limit,
	df['Age'])
)
print(df)

print()

# Feature Scaling
from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler_minmax = MinMaxScaler()
df['Attendence_Normalized'] = scaler_minmax.fit_transform(df[['Attendance']])
print(df)

print()

scaler_std =  StandardScaler()
df['Salary_Standardized'] = scaler_std.fit_transform(df[['Salary']])
print(df)


### Encording catogorical Data  ##

from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

#Lable Encoding

print("Lable Encoding")

le = LabelEncoder()
df['Department'] = le.fit_transform(df['Department'])
print(df.info())

df=pd.get_dummies(df,columns=['Gender'],dtype=int)
print("\n--6.After Categorical Encoding ---")
print(df.info())

#save Cleaned Dataset

df.to_csv('./student_cleaned.csv',index=False)
print("Saved database")



















