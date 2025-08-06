import pandas as pd
import statsmodels.api as sm

# 1. Load dataset
df = pd.read_csv('AI_Impact_on_Jobs.csv')

# 2. Keep relevant columns
df_q10 = df[["Automation Risk (%)", "Location", "Required Education", "Remote Work Ratio (%)"]].copy()

# 3. Fix text encoding in Required Education column
df_q10["Required Education"] = df_q10["Required Education"].str.replace("â€™", "'")

# 4. Convert categorical variables into dummy variables
df_encoded = pd.get_dummies(df_q10, columns=["Location", "Required Education"], drop_first=True)

# 5. Define dependent (Y) and independent (X) variables
Y = df_encoded["Automation Risk (%)"]
X = df_encoded.drop(columns=["Automation Risk (%)"])

# 6. Add constant term for intercept
X = sm.add_constant(X)

# 7. Build the regression model
model = sm.OLS(Y, X).fit()

# 8. Display summary
print(model.summary())