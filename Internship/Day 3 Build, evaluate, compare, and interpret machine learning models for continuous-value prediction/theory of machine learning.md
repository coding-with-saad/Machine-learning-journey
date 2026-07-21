# Now Let's Understand the Theory

---

# What is Regression?

Regression predicts a **number**.

Examples:

| Input              | Output      |
| ------------------ | ----------- |
| House size         | House price |
| Study hours        | Exam score  |
| Experience         | Salary      |
| Advertising budget | Sales       |

Notice that the output is a **continuous numerical value**.

Examples:

```text
$350,000

78.4

12.5

250.8
```

Regression predicts numbers.

---

# Dependent and Independent Variables

This is the foundation of regression.

Example:

Predict exam score.

Inputs:

```text
Study Hours

Attendance

Assignments
```

Output:

```text
Exam Score
```

The inputs are called **independent variables** (also known as **features**).

The output is called the **dependent variable** (also known as the **target**).

Example:

```
Study Hours --------\
Attendance -----------> Exam Score
Assignments ---------/
```

---

# Linear Relationship

Suppose:

| Study Hours | Exam Score |
| ----------- | ---------- |
| 1           | 40         |
| 2           | 50         |
| 3           | 60         |
| 4           | 70         |

The points form a straight-line trend.

This is a **linear relationship**.

If the relationship is curved, then it is **non-linear**.

---

# Regression Assumptions

Every regression model assumes certain conditions.

Some common assumptions are:

* Relationship is approximately linear.
* Errors are random.
* Errors have similar variance (homoscedasticity).
* Features are not highly correlated with each other (for linear regression).

These assumptions help ensure the model's predictions are reliable.

---

# Residuals

Residual =

```text
Actual Value

-

Predicted Value
```

Example:

Actual score

```text
80
```

Model predicted

```text
75
```

Residual

```text
5
```

Residuals tell you how far the predictions are from the real values.

Good models have small residuals.

---

# Multicollinearity

Suppose your features are:

```
Study Hours

Hours Studied

Time Spent Studying
```

All three describe almost the same thing.

This can confuse some regression models, especially linear regression.

This issue is called **multicollinearity**.

---

# Algorithms

These are different ways to build regression models.

---

## 1. Simple Linear Regression

Uses **one input feature**.

```
Study Hours

↓

Exam Score
```

One feature predicts one output.

---

## 2. Multiple Linear Regression

Uses **multiple input features**.

```
Study Hours

Attendance

Assignments

↓

Exam Score
```

This is more common in real projects.

---

## 3. Polynomial Regression

Useful when the relationship is curved rather than straight.

Instead of fitting a straight line, it fits a curve.

---

## 4. Ridge Regression

Linear regression with regularization.

It helps reduce overfitting by shrinking large coefficients.

---

## 5. Lasso Regression

Similar to Ridge, but it can also eliminate less important features by reducing some coefficients to zero.

---

## 6. Elastic Net

Combines ideas from both Ridge and Lasso.

---

## 7. Decision Tree Regressor

Instead of fitting a line, it learns a series of decision rules.

Example:

```
Study Hours > 5 ?

      Yes

        ↓

Predict 85

      No

        ↓

Predict 60
```

---

## 8. Random Forest Regressor

Builds many decision trees and averages their predictions.

This usually improves accuracy and reduces overfitting.

---

## 9. Gradient Boosting Regressor

Builds trees one after another.

Each new tree focuses on correcting the mistakes made by previous trees.

---

## 10. XGBoost / LightGBM

These are advanced boosting algorithms.

They are popular in machine learning competitions and many industry projects because they are often very accurate and efficient.

---

# Evaluation Metrics

These tell you how well your model predicts.

---

## MAE (Mean Absolute Error)

Average absolute prediction error.

Smaller is better.

---

## MSE (Mean Squared Error)

Squares the errors before averaging them.

Large mistakes are penalized more.

---

## RMSE

Square root of MSE.

It is easier to interpret because it uses the same units as the target variable.

---

## R² (R-squared)

Measures how much of the variation in the target is explained by the model.

Typical range:

```
0 → Poor

1 → Perfect
```

Higher is better.

---

## Adjusted R²

Similar to R² but adjusts for the number of input features.

Useful when comparing models with different numbers of features.

---

## MAPE

Average percentage error.

Example:

```
Actual = 100

Predicted = 90

Error = 10%
```

---

# Model Behaviour

---

## Bias

The model is too simple and misses important patterns.

---

## Variance

The model is too sensitive to the training data.

---

## Underfitting

The model is too simple.

Training accuracy is low.

Testing accuracy is also low.

---

## Overfitting

The model memorizes the training data.

Training accuracy is high.

Testing accuracy is poor.

---

## Learning Curves

These plots show how training and validation performance change as the amount of training data increases.

They help identify underfitting and overfitting.

---

## Residual Analysis

After training a model, plot the residuals.

If the residuals are randomly scattered around zero, that's generally a good sign.

Patterns in residuals may indicate problems with the model.

---

# Cross-Validation

Instead of splitting the data only once into training and testing sets, cross-validation evaluates the model on multiple different splits.

This provides a more reliable estimate of model performance.

---

## K-Fold Cross-Validation

Example with 5 folds:

```
Fold 1 → Test

Fold 2 → Test

Fold 3 → Test

Fold 4 → Test

Fold 5 → Test
```

Each fold gets a turn as the test set.

---

## Repeated Cross-Validation

Runs K-fold multiple times with different random splits.

This produces even more stable evaluation results.

---

