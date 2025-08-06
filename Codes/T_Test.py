import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("AI_Impact_on_Jobs.csv")

# Filter for only High and Low AI Impact Levels
df_filtered = df[df['AI Impact Level'].isin(['High', 'Low'])]
print(df_filtered)
# Drop rows with missing Remote Work Ratio values
df_filtered = df_filtered.dropna(subset=['Remote Work Ratio (%)'])

# Create two groups
remote_high = df_filtered[df_filtered['AI Impact Level'] == 'High']['Remote Work Ratio (%)']
remote_low = df_filtered[df_filtered['AI Impact Level'] == 'Low']['Remote Work Ratio (%)']

# Perform Welch's t-test (assumes unequal variances)
t_stat, p_val = stats.ttest_ind(remote_high, remote_low, equal_var=False)

# Print the results
print("T-statistic:", t_stat)
print("P-value:", p_val)

if p_val < 0.05:
    print("Result: Significant difference in remote work ratio between High and Low AI impact jobs.")
else:
    print("Result: No significant difference in remote work ratio.")

# Visualize the result
sns.boxplot(x='AI Impact Level', y='Remote Work Ratio (%)', data=df_filtered)
plt.title('Remote Work Ratio by AI Impact Level')
plt.ylabel('Remote Work Ratio (%)')
plt.xlabel('AI Impact Level')
plt.show()