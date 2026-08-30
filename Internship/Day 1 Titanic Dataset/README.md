# Day 1: Titanic Dataset Exploration

## Overview
This directory contains the initial work on the Titanic Passenger dataset. It marks the transition from pure Python syntax practice to actual data manipulation and exploratory data analysis (EDA) using the Pandas library.

## Contents
- **`Titanic-Dataset.csv`**: The raw passenger dataset containing columns like PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, and Embarked.
- **`titanic data set.zip`**: A compressed archive of the raw dataset.
- **`dataset.py`**: A python script that:
  - Loads the CSV data using Pandas (`pd.read_csv`).
  - Displays the first five passenger records using `df.head()`.
  - Generates and outputs summary statistics of numerical columns using `df.describe()`.

## Key Learning Outcomes
- Introduction to the Pandas library for data loading and manipulation.
- Basic dataset shape inspection and exploratory statistics.
