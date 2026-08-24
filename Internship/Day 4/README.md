# Day 4: Quality Assurance Audit & Model Validation

## Overview
This folder contains the quality assurance and software quality engineering (SQE) audit materials. On Day 4, a strict validation suite was implemented to check dataset health, model output stability, and correct prediction behavior between Jupyter calculations and Streamlit frontend results.

## Key Files
| File Name | File Type | Description |
| :--- | :--- | :--- |
| [SQE.ipynb](file:///D:/Machine%20Learning/Machine%20Learning/Internship/Day%204/SQE.ipynb) | Jupyter Notebook | Audit execution notebook carrying tests for dataset shape, duplicate rows, missing values, scaler bounds, and prediction matching. |
| [qa_results.pkl](file:///D:/Machine%20Learning/Machine%20Learning/Internship/Day%204/qa_results.pkl) | Pickle Serialization | Serialized test results capturing the status (PASS/FAIL) and logs of each executed audit test. |
| [Quality_Assurance_Audit_Report.pdf](file:///D:/Machine%20Learning/Machine%20Learning/Internship/Day%204/Quality_Assurance_Audit_Report.pdf) | PDF Document | Formal report compiling the results, methodology, and metrics of the QA audit. |
| [AI_Lab_99_QA_Audit_Poster.pdf](file:///D:/Machine%20Learning/Machine%20Learning/Internship/Day%204/AI_Lab_99_QA_Audit_Poster.pdf) | PDF Document | Audit overview poster detailing the compliance checks and results. |

## Activities & Processes
1. **Dataset Integrity Audit**: Verified the shape of `Final Dataset.csv` (2,216 rows, 39 columns), confirmed 0 duplicate rows, and checked for missing data. Checked key columns like `Income` and `Total_spending` for data types and scaling consistency.
2. **Model Deserialization Check**: Checked that `kmeans_model.pkl` loaded properly and expected exactly 10 features (`n_features_in_ = 10`).
3. **Prediction Consistency Validation**: Tested predictions on dummy records across multiple methods to ensure the scaler and clustering coefficients computed in Jupyter match Streamlit's calculations perfectly.
4. **Compiled QA Test Run**: Configured a dictionary of 16 QA checks evaluating all assets, outputting a 100% test pass status. Saved results inside `qa_results.pkl`.
