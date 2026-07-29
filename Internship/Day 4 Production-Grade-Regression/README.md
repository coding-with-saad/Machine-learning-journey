# NYC Taxi ETA Prediction — Advanced Regression Project

## Project Overview
This project builds a regression system to predict **taxi trip duration (in minutes)** at the moment a trip is requested, using NYC TLC Yellow Taxi trip data. The goal is to create a deployment-safe, leakage-free, and explainable model.

---

## Day 1 — Problem Framing, Data Audit & EDA

### 1. Dataset Used
- **Source:** NYC TLC Yellow Taxi Trip Records — January 2023
- **Format:** CSV
- **Rows loaded:** 500,000 (subset used for development; full dataset is ~2GB / several million rows)
- **Tool:** Jupyter Notebook, pandas, matplotlib, seaborn

> Note: A 500,000-row subset (`nrows=500000`) was used during development for faster iteration. The full dataset will be used in later stages once the pipeline is validated.

### 2. Business Problem Statement
- **Business Objective:** Provide passengers with an estimated trip duration before the trip begins.
- **Prediction Target:** Trip duration in minutes.
- **Prediction Moment:** At the time a trip is requested (before pickup).
- **Intended Users:** Passenger-facing app, dispatch system, drivers.
- **Business Value:** Improved trust, better planning, more accurate ETAs.
- **Cost of Underprediction:** Passenger arrives late relative to expectation, reduces trust in the platform.
- **Cost of Overprediction:** Passenger may over-wait or switch to a competing service.
- **Data Limitations:** Only 2023 data used; no weather or live traffic data included.
- **Deployment Assumptions:** Only features available *before* the trip starts will be used for modeling (see Leakage Audit below).

### 3. Target Variable Creation
```python
trip_duration_minutes = (tpep_dropoff_datetime - tpep_pickup_datetime).total_seconds() / 60
```
- Dropoff timestamp is removed after target creation to prevent leakage.
- Distribution checked for zero, negative, and implausible durations.

### 4. Data Audit Summary

| Check                | Result                              |
| -------------------- | ----------------------------------- |
| Original rows loaded | 500,000                             |
| Rows after cleaning  | 494,634                             |
| Rows removed         | 5,366                               |
| Missing values       | Checked via `df.isnull().sum()`     |
| Duplicate rows       | Checked via `df.duplicated().sum()` |

**Filtering thresholds applied:**
- `trip_duration_minutes >= 1` → trips under 1 minute treated as invalid/erroneous records.
- `trip_duration_minutes <= 180` → trips over 3 hours treated as outliers (likely meter/data errors).
- `trip_distance > 0` → zero-distance trips are invalid.
- `passenger_count > 0` → zero-passenger trips are invalid.

These thresholds were chosen to remove clearly erroneous records while preserving the natural range of realistic NYC taxi trips. They will be revisited if EDA reveals they are too aggressive or too lenient.

### 5. Exploratory Data Analysis (EDA)
The following visualizations were generated on the cleaned dataset (`df_clean`):

1. **Trip Duration Distribution** — histogram showing a right-skewed distribution (many short trips, few very long ones).
2. **Log Trip Duration Distribution** — log1p transform applied to reduce skew for modeling purposes.
3. **Duration by Pickup Hour** — boxplot showing how trip duration varies across the day.
4. **Duration by Day of Week** — boxplot showing weekday vs weekend patterns.
5. **Trip Count by Hour** — bar chart identifying peak demand hours.
6. **Passenger Count Distribution** — countplot of passenger counts per trip.
7. **Correlation Matrix** — heatmap of numeric features (duration, distance, passenger count, fare, hour).

> Borough-level EDA (pickup/dropoff borough) was deferred to Day 2, pending merge with the Taxi Zone Lookup Table.

### 6. Key Observations (fill in after reviewing your graphs)
- Trip duration is right-skewed; log transform produces a more normal-shaped distribution.
- [Add your own observation: e.g., which hours have longer trip durations]
- [In 7pm to 8pm Number of Trips per Hour is Increase Approximetly 32000/33000 ]
- [Add your own observation: e.g., correlation between distance and duration]

---

## Next Steps → Day 2
- Merge Taxi Zone Lookup Table for borough-level features.
- Build baseline models (Mean Predictor, Median Predictor, Median by Route, Median by Hour & Route).
- Begin feature engineering (time-based, geographic, interaction features).

---

## Repository Structure
```
week03-advanced-regression/
│
├── README.md
├── requirements.txt
├── configs/
├── data/
├── notebooks/
├── src/
├── tests/
├── models/
├── reports/
└── presentation/
```