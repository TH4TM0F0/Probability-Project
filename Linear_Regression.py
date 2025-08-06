import pandas as pd 
import matplotlib.pyplot as plt  

data = pd.read_csv("AI_Impact_on_Jobs.csv")

from sklearn.linear_model import LinearRegression

model = LinearRegression()
X = data[['Experience Required (Years)']]  
y = data['Job Openings (2024)']

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, label='Data points')
plt.plot(X, y_pred, color='black', label='Regression line')

# Add labels
plt.xlabel("Impact Level")              
plt.ylabel("Remote Work Ratio")           
plt.title("Linear Regression using Scikit-Learn")
plt.legend()
plt.show()

# Print model coefficients
print("Slope (coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R² score:", model.score(X, y))