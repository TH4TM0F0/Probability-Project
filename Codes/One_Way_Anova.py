import pandas as pd

# Load your dataset
data = pd.read_csv("AI_Impact_on_Jobs.csv")

# Prepare a summary table by industry
industry_summary = data.groupby("Industry")["Median Salary (USD)"].agg(["count", "mean"])
industry_summary.rename(columns={"count": "Number of Jobs", "mean": "Average Salary (USD)"}, inplace=True)

# Display the table
print(industry_summary)


grand_mean = data['Median Salary (USD)'].mean()
print("Grand Mean = ", grand_mean)


# For SSA 
SSA = sum(
    row["Number of Jobs"] * (row["Average Salary (USD)"] - grand_mean) ** 2
    for _, row in industry_summary.iterrows()
)

print("SSA = ", SSA)


# For SST
SST = ((data['Median Salary (USD)'] - grand_mean) ** 2).sum()

print("SST = ", SST)


# For SSE
SSE = SST - SSA
print("SSE = ", SSE)


# Anova Table
degreeOfFreeedom_1 = 7
degreeOfFreeedom_2 = 29992


MSA = SSA / degreeOfFreeedom_1
MSE = SSE / degreeOfFreeedom_2
F = MSA / MSE

print("S1 sqaured = ", MSA)
print("S squared = ", MSE)
print("F = ", F)