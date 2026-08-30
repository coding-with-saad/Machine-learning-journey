# Titanic Data Preprocessing & Feature Engineering

## Overview
This directory represents the data cleaning, feature engineering, and preparation stages for the Titanic passenger survival dataset. The objective is to build a robust, repeatable preprocessing pipeline that transforms messy, raw data into a clean structure ready for machine learning models, avoiding target leakage.

## Contents
- **`2.Titanic.ipynb`**: A Jupyter notebook that develops the step-by-step preprocessing steps:
  - Data loading and quality audit.
  - Handling missing data (e.g., dropping high-missing columns like `deck`, imputing age/fare).
  - Outlier detection and treatment.
  - Engineering features such as `Family Size` (SibSp + Parch + 1) and an indicator `Is_Alone`.
  - Encoding categorical variables using LabelEncoder.
  - Scaling numerical variables (Age, Fare, FamilySize).
- **`preprocessing_pipeline.joblib`**: Serialized preprocessing pipeline using Joblib, ensuring reproducibility for training/test sets and deployment.
- **`cleaned_dataset.csv`**: The resulting fully preprocessed dataset.
- **`X_train.csv` & `y_train.csv`**: Split training features and target labels.
- **`X_test.csv` & `y_test.csv`**: Split testing features and target labels.
- **`Titanic Dataset Data Preprocessing and Feature Engineering Report.pdf`**: A formal report detailing the methodologies, decisions, and transformations applied to the data.

## Key Learning Outcomes
- Cleaning messy data, handling missing values, and engineering domain-specific features.
- Implementing label encoding and numerical scaling.
- Saving preprocessors using serialization (`joblib`) to prevent data leakage.
