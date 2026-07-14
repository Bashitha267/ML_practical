from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

import numpy as np
df=pd.read_csv('student_data.csv')
scaler_minmax = MinMaxScaler()

df = pd.read_csv("student_data.csv")

print("Before")
print(df)

df["Attendance_Normalized"] = scaler_minmax.fit_transform(
    df[["Attendance"]]
)

print(df)