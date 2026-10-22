# Import the linear regression model from scikit-learn
from sklearn.linear_model import LinearRegression
import pandas as pd

# Read the dataset from the CSV file
sales_df = pd.read_csv("advertising_sales.csv")

# Create the feature matrix X and target vector y
# X contains the radio advertising values, reshaped into a 2D array
# y contains the sales values we want to predict
X = sales_df["radio"].values.reshape(-1, 1)
y = sales_df["sales"].values

# Create a linear regression model object
reg = LinearRegression()

# Train the model using the input features X and target y
reg.fit(X, y)

# Use the trained model to make predictions on the same data
predictions = reg.predict(X)

# Display the first 5 predictions
print(predictions[:5])