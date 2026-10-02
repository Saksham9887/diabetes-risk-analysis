import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("diabetes.csv")

# First 5 rows
print("\nFIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Diabetes outcome count
outcome_count = df['Outcome'].value_counts()

print("\nDIABETES OUTCOME COUNT")
print(outcome_count)

# Compare averages between diabetic and non-diabetic groups
print("\nAVERAGE VALUES BY OUTCOME (0 = No Diabetes, 1 = Diabetes)")
group_means = df.groupby('Outcome')[['Glucose', 'BMI', 'Age', 'BloodPressure', 'Insulin']].mean()
print(group_means)

# Correlation of each feature with the diabetes outcome
print("\nCORRELATION WITH DIABETES OUTCOME")
correlations = df.corr(numeric_only=True)['Outcome'].sort_values(ascending=False)
print(correlations)

# Pie chart
plt.figure(figsize=(6,6))

plt.pie(
    outcome_count,
    labels=['No Diabetes', 'Diabetes'],
    autopct='%1.1f%%'
)

plt.title("Diabetes Distribution")

plt.show()

# Glucose vs BMI scatter plot
plt.figure(figsize=(8,6))

plt.scatter(df['Glucose'], df['BMI'])

plt.title("Glucose vs BMI")
plt.xlabel("Glucose")
plt.ylabel("BMI")

plt.show()

# Histogram of Age
plt.figure(figsize=(8,6))

plt.hist(df['Age'])

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.show()

# Average glucose level
avg_glucose = df['Glucose'].mean()

print("\nAVERAGE GLUCOSE LEVEL:", avg_glucose)

# Glucose vs BMI, colored by diabetes outcome
plt.figure(figsize=(8,6))
colors = df['Outcome'].map({0: 'blue', 1: 'red'})
plt.scatter(df['Glucose'], df['BMI'], c=colors, alpha=0.6)
plt.title("Glucose vs BMI (red = diabetic, blue = non-diabetic)")
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.show()