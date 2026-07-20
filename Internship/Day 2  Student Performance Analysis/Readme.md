# 📊 Student Performance Analysis using Python

## 📌 Project Overview

This project analyzes student academic performance using Python and basic statistical techniques. The objective is to explore relationships between different academic factors such as study hours, attendance, assignment scores, and exam performance. The project demonstrates how data analysis can be used to extract meaningful insights from educational datasets.

The analysis includes descriptive statistics, probability, correlation analysis, normal distribution, outlier detection, and data visualization.

---

# 🎯 Project Objectives

The primary objectives of this project are to:

* Analyze student performance using Python.
* Apply fundamental statistical concepts to real-world data.
* Identify relationships between different academic factors.
* Detect unusual observations (outliers).
* Visualize data using graphs.
* Generate meaningful recommendations based on the analysis.

---

# 📂 Dataset

The project uses a CSV dataset named:

```text
student_performance.csv
```

## Dataset Columns

| Column           | Description                        |
| ---------------- | ---------------------------------- |
| Student_ID       | Unique identifier for each student |
| Study_Hours      | Average study hours of the student |
| Attendance       | Attendance percentage              |
| Assignment_Score | Assignment marks                   |
| Exam_Score       | Final exam marks                   |

The dataset contains data for at least **20 students**.

---

# 🛠 Technologies Used

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* SciPy

---

# 📚 Python Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
```

---

# 📈 Project Tasks

## Task 1: Descriptive Statistics

### Purpose

Understand the overall performance of students by calculating the basic statistical measures of the exam scores.

### Calculations

* Mean
* Median
* Mode
* Variance
* Standard Deviation

### Outcome

This task provides a summary of student performance and shows how exam scores are distributed around the average.

---

## Task 2: Percentiles and Quartiles

### Purpose

Analyze the distribution of exam scores and identify where most students fall within the dataset.

### Calculations

* 25th Percentile (Q1)
* 50th Percentile (Median)
* 75th Percentile (Q3)
* Minimum Score
* Maximum Score

### Outcome

Determines the score range of the middle 50% of students and helps understand score distribution.

---

## Task 3: Correlation Analysis

### Purpose

Identify which academic factor has the strongest relationship with exam performance.

### Correlation Analysis

* Study Hours vs Exam Score
* Attendance vs Exam Score
* Assignment Score vs Exam Score

### Visualization

Scatter Plot

### Outcome

Determines which factor most strongly influences exam scores.

---

## Task 4: Probability Analysis

### Purpose

Estimate the likelihood of different academic outcomes using empirical probability.

### Calculations

* Probability of passing (Exam Score ≥ 50)
* Probability of scoring 80 or above
* Probability of studying more than 5 hours

### Outcome

Provides statistical probabilities based on the available student data.

---

## Task 5: Normal Distribution Analysis

### Purpose

Determine whether exam scores approximately follow a normal distribution.

### Analysis

* Histogram of Exam Scores
* Z-Score Calculation
* Identification of students with Z-Score greater than ±2

### Outcome

Highlights unusually high or low performers and evaluates score distribution.

---

## Task 6: Outlier Detection

### Purpose

Detect abnormal exam scores that differ significantly from the rest of the dataset.

### Method Used

Interquartile Range (IQR)

```text
IQR = Q3 − Q1

Lower Bound = Q1 − 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

### Visualization

Box Plot

### Outcome

Identifies potential outliers and visualizes score spread.

---

# 📊 Data Visualizations

The project generates the following graphs:

* Histogram of Exam Scores
* Scatter Plot (Highest Correlation)
* Box Plot for Outlier Detection

These visualizations make it easier to understand data patterns and relationships.

---

# 📋 Final Project Report

The final report includes:

* Statistical summary of student performance
* Strongest factor associated with exam scores
* Probability of passing the exam
* Identified outliers
* Two recommendations for improving student performance

---

# 📁 Project Structure

```text
Student_Performance_Analysis/
│
├── student_performance.csv
├── analysis.ipynb
├── analysis.py
├── README.md
│
├── images/
│   ├── histogram.png
│   ├── scatter_plot.png
│   └── boxplot.png
│
└── report.docx
```

---

# 🚀 How to Run the Project

## 1. Clone the repository

```bash
git clone <repository-url>
cd Student_Performance_Analysis
```

## 2. Install dependencies

```bash
pip install pandas numpy matplotlib scipy
```

## 3. Run the analysis

Using Jupyter Notebook:

```bash
jupyter notebook
```

or

```bash
python analysis.py
```

---

# 📦 Project Deliverables

* ✅ Python Notebook (`analysis.ipynb`) or Python Script (`analysis.py`)
* ✅ Student dataset (`student_performance.csv`)
* ✅ Histogram
* ✅ Scatter Plot
* ✅ Box Plot
* ✅ One-page project summary/report

---

# 📖 Learning Outcomes

After completing this project, you will understand:

* Reading and processing CSV files using Pandas
* Data manipulation with Python
* Descriptive statistics
* Percentiles and quartiles
* Correlation analysis
* Empirical probability
* Normal distribution and Z-scores
* Outlier detection using the IQR method
* Data visualization with Matplotlib
* Presenting analytical findings through reports

---

# 💡 Future Improvements

Possible enhancements include:

* Analyze larger datasets with hundreds or thousands of students.
* Build an interactive dashboard using Streamlit or Dash.
* Add machine learning models to predict exam scores.
* Create interactive visualizations with Plotly.
* Connect the project to a SQL database for real-time analysis.

---

# 👨‍💻 Author
**Malik Saad Khawar**

**Developed as part of a Python Data Analysis Internship Project**

This project demonstrates practical applications of Python, statistics, and data visualization for educational data analysis.
