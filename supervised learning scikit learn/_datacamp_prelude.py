# ============================================================
# DataCamp environment: Supervised Learning with scikit-learn
# Auto-prepended by dcpush to every file pushed into this folder.
# ============================================================
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# DataCamp preloads this dataset as `sales_df`.
sales_df = pd.read_csv("advertising_sales.csv")

# Default X/y for the simple linear regression exercises.
# Override these in your snippet if the exercise defines its own.
X = sales_df[["radio"]].values
y = sales_df["sales"].values

# `predictions` is preloaded on the visualization and residual exercises.
# Fitted here on the same X/y so the file runs standalone.
predictions = LinearRegression().fit(X, y).predict(X)
