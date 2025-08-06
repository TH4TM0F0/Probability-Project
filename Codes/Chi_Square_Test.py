import pandas as pd              
from scipy.stats import chi2_contingency 
import seaborn as sns            
import matplotlib.pyplot as plt  

# Load the Dataset from the CSV file
dataSet = pd.read_csv("AI_Impact_on_Jobs.csv")

# Filtering the Data
cleanedData = dataSet[['AI Impact Level', 'Industry']].dropna()


#Creating the Continngency table
contingency_table = pd.crosstab(cleanedData['Industry'], cleanedData['AI Impact Level'])
print(contingency_table)


# Computing the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)


# Printing the Expected table]
expected_df = pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns)
print(expected_df)


# Print the results
print("Chi-Square Statistic:", chi2)
print("Degrees of Freedom:", dof)
print("P-value:", p)



plt.figure(figsize=(10, 6))
sns.heatmap(contingency_table, annot=True, fmt="d", cmap="YlGnBu")

plt.title("Distribution of AI Impact Levels Across Industries")
plt.xlabel("AI Impact Level")
plt.ylabel("Industry")
plt.tight_layout()
plt.show()