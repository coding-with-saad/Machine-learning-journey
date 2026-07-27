# Data Cleaning, Preprocessing and Feature Engineering

## Overview

This project demonstrates a complete machine learning data preprocessing workflow using two Kaggle datasets. It covers data quality assessment, missing value handling, categorical encoding, feature engineering, data splitting, leakage prevention, and reusable preprocessing pipelines using Scikit-Learn.

---

## Objectives

- Improve data quality by identifying and correcting common issues.
- Compare different missing value imputation techniques.
- Encode categorical variables appropriately.
- Scale numerical features using multiple methods.
- Create meaningful engineered features.
- Prevent data leakage during preprocessing.
- Build reusable preprocessing pipelines.

---

## Datasets

### Dataset 1
House Prices Prediction Dataset

Used for:
- Missing value treatment
- Outlier detection
- Feature engineering
- Numerical scaling

### Dataset 2
Titanic Dataset

Used for:
- Categorical encoding
- Missing value handling
- Data splitting
- Pipeline implementation

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook

---

## Topics Covered

### Data Quality
- Missing values
- Duplicate records
- Invalid values
- Inconsistent categories
- Incorrect data types
- Outlier detection
- Noisy data treatment

### Missing Value Treatment
- Row deletion
- Column deletion
- Mean imputation
- Median imputation
- Mode imputation
- SimpleImputer

### Categorical Data
- Label Encoding
- Ordinal Encoding
- One-Hot Encoding
- High-cardinality handling
- Rare-category handling

### Numerical Data
- StandardScaler
- MinMaxScaler
- RobustScaler
- Log transformation
- Outlier treatment

### Feature Engineering
- Derived features
- Date and time features
- Text length features
- Ratio features
- Binning
- Interaction features
- Domain-specific features

### Data Splitting
- Random split
- Validation split
- Stratified split
- Time-based split

### Data Leakage
- Target leakage
- Training-test contamination
- Proper preprocessing order
- Future information leakage

### Scikit-Learn Pipelines
- Pipeline
- ColumnTransformer
- Reusable preprocessing
- Reproducible workflow

---

## Project Structure

```text
Data_Preprocessing_Project/
│
├── dataset1/
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   └── notebook.ipynb
│
├── dataset2/
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   └── notebook.ipynb
│
├── pipeline.py
├── preprocessing_report.pdf
├── requirements.txt
└── README.md
```

---

## Results

- Cleaned both datasets successfully.
- Compared multiple imputation techniques.
- Encoded categorical features.
- Scaled numerical variables using three scaling methods.
- Engineered new informative features.
- Built reusable preprocessing pipelines.
- Demonstrated techniques to avoid data leakage.

---

## Conclusion

This project demonstrates a complete preprocessing workflow commonly used in machine learning projects. It provides a reproducible and scalable approach for preparing raw data before model training while following best practices to ensure data quality and prevent leakage.

---

## Author

**Saad Khawar**

GitHub: https://github.com/coding-with-saad