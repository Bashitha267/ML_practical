import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('./student_cleaned.csv')
# print(df)

# plt.figure(figsize=(6,5))

# gender_count_male = df['Gender_Male'].sum()
# gender_count_female = df['Gender_Female'].sum()


# plt.bar(['Male','Female'],[gender_count_male,gender_count_female],
#         color=['skyblue', 'pink'])

# plt.title('Bar Chart -> Count of Gender')
# plt.xlabel('Gender')
# plt.ylabel('Count')

# plt.show()

# print("Scatter Plot")
# plt.figure(figsize=(8,6))
# plt.scatter(df['Age'],df['GPA'],color='purple')
# plt.title('Scatter Plot -> Age vs GPA')
# plt.show()

plt.figure(figsize=(8,6))
corr=df[['Age','GPA','Attendance','Salary']].corr()
sb.heatmap(corr,annot=True,cmap='coolwarm',center=0,linewidths=0.5)
plt.title('Heatmap Correlation')
plt.show()