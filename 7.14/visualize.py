import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('./student_data_cleaned.csv')
print(df)

plt.figure(figsize=(6,5))

gender_count = df['Gender'].value_counts()

plt.bar(gender_count.index, gender_count.values,
        color=['skyblue', 'pink'])

plt.title('Bar Chart -> Count of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

plt.show()