# ML Foundations

This repository is organized by topic so each notebook/script is easy to find and understand.

## Folder Structure

- `ml_foundations/`
  - `pandas_basics.ipynb`: Introductory pandas concepts.
- `numpy/`
  - `numpy_overview.ipynb`: Core NumPy concepts.
  - `numpy_basics.ipynb`: NumPy basics and fundamentals.
  - `numpy_array_operations.ipynb`: Common array operations.
  - `numpy_exercises_ml.ipynb`: NumPy practice exercises for ML prep.
- `pandas/`
  - `pandas_dataframes.ipynb`: DataFrame-focused practice.
  - `pandas_missing_data.ipynb`: Missing data handling techniques.
  - `pandas_groupby_aggregation.ipynb`: GroupBy and aggregation techniques.
  - `pandas_pivot_tables.ipynb`: Pivot table exercises.
- `linear_regression/`
  - `linear_regression_prepare_features.py`: Builds feature/target arrays from advertising data.
  - `linear_regression_train_test_split.py`: Train/test split linear regression workflow and predictions.
  - `advertising_sales.csv`: Dataset for regression exercises.
- `supervised_learning_scikit_learn/`
  - `datacamp_prelude.py`: Shared setup data and defaults for exercises.
  - `linear_regression_fit_predict.py`: Fits a simple regression and generates predictions.
  - `plot_radio_vs_sales.py`: Visualizes the radio vs sales relationship.
  - `evaluate_regression_metrics.py`: Computes regression performance metrics (R² and RMSE).
  - `advertising_sales.csv`: Dataset used in supervised learning scripts.
- `pandas_merging_joining_concatenation.ipynb`
  - Notebook covering pandas merge, join, and concatenation patterns.

## Codebase Analysis Summary

- Most Python files are small, exercise-focused scripts for scikit-learn linear regression.
- Notebooks are primarily grouped around NumPy and pandas fundamentals.
- Regression scripts rely on local CSV files and shared variable context (`X`, `y`, `reg`, `y_test`, `y_pred`) in exercise flow.
- Naming now reflects each file's actual purpose so new learners can navigate topics quickly.
