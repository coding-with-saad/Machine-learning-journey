# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

# df = pd.read_csv("Housing.csv")
# # print(df.head())

# print(df.shape)
# print(df.info())
# print(df.describe())

# print(df.isnull().sum())

# X = df.drop("price", axis=1)

# y = df["price"]


# ==============================
# 1. Import Required Libraries
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Machine Learning Libraries
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet
)
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Evaluation Metrics
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

df = pd.read_csv("Housing.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

print(df.isnull().sum())

binary_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for column in binary_columns:
    df[column] = df[column].map({
        "yes": 1,
        "no": 0
    })

df = pd.get_dummies(
    df,
    columns=["furnishingstatus"],
    drop_first=True
)

print(df.head())