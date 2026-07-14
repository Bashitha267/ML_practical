from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
import pandas as pd
import numpy as np

df = pd.read_csv('student_data.csv')

le = LabelEncoder()
df['Department'] = le.fit_transform(df['Department'])

print(df)