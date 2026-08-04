# NYC Taxi ETA Prediction — Advanced Regression Project

## Project Overview
This project builds a regression system to predict **taxi trip duration (in minutes)** at the moment a trip is requested, using NYC TLC Yellow Taxi trip data (January 2023, 500,000-row development sample). The project follows a production-oriented ML workflow: leakage prevention, feature engineering, model comparison, cross-validation, error analysis, and explainability.

---

## Dataset
- **Source:** NYC TLC Yellow Taxi Trip Records — January 2023 (`.parquet`)
- **Sample size:** 500,000 rows (development phase)
- **Zone reference:** NYC Taxi Zone Lookup Table (265 zones, merged on `LocationID`)
- **Target variable:** `trip_duration_minutes = (dropoff_datetime - pickup_datetime).total_seconds() / 60`

---

## Day 1 — Problem Framing, Data Audit & EDA

### Business Problem
- **Objective:** Estimate trip duration before a trip begins, for passenger-facing ETA display.
- **Prediction moment:** At trip request, before pickup.
- **Cost of underprediction:** Passenger arrives later than expected, reducing trust.
- **Cost of overprediction:** Passenger over-waits or switches providers.
- **Deployment assumption:** Only pre-trip information may be used (see Leakage Audit).

### Data Cleaning
| Step               | Rows    |
| ------------------ | ------- |
| Original (sampled) | 500,000 |
| After cleaning     | 494,634 |
| Removed            | 5,366   |

**Filtering thresholds:** duration between 1–180 minutes, trip distance > 0, passenger count > 0. Thresholds were chosen to remove clearly erroneous records (meter/data errors) while preserving realistic NYC trip ranges.

### EDA Highlights
- Trip duration is right-skewed; log transform produces a more symmetric distribution.
- Duration varies meaningfully by hour of day and day of week, motivating time-based features.
- Correlation matrix showed trip distance and duration are related but not sufficient alone (motivating richer feature engineering).

---

## Day 2 — Feature Engineering

Zone lookup table merged on `PULocationID`/`DOLocationID` → `LocationID` (dtype mismatch had to be fixed via `Int64` casting).

**14 deployment-safe features created**, exceeding the 12-feature minimum:

| Category    | Features                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------- |
| Time        | `pickup_hour`, `pickup_month`, `pickup_dayofweek`, `is_weekend`, `is_peak_hour`, `is_night` |
| Cyclical    | `hour_sin`, `hour_cos`                                                                      |
| Geographic  | `same_borough`, `is_pickup_manhattan`, `is_airport_route`, `route_pair`                     |
| Interaction | `pickup_zone_hour`, `weekend_borough`                                                       |

All features are available before trip start, satisfying the deployment-safety requirement.

---

## Day 3 — Baseline & Linear Models

### Baseline Models
| Model                      | MAE (minutes) |
| -------------------------- | ------------- |
| Mean Predictor             | 10.03         |
| Median Predictor           | 9.44          |
| Median by Route            | 5.08          |
| **Median by Hour & Route** | **4.19**      |

The Hour+Route median baseline is effectively a lookup table of historical averages — a strong, hard-to-beat benchmark for models that don't see this signal directly.

### Linear & Regularized Models
| Model             | MAE   |
| ----------------- | ----- |
| Linear Regression | 7.264 |
| Ridge             | 7.262 |
| Lasso             | 7.596 |
| Elastic Net       | 7.593 |

**Finding:** Ridge ≈ Linear Regression, indicating minimal overfitting in the base feature set. Lasso/Elastic Net perform slightly worse — their coefficient shrinkage likely removes features that carry useful (if weak) signal.

---

## Day 4 — Tree & Ensemble Models

| Model                                       | MAE       |
| ------------------------------------------- | --------- |
| Decision Tree                               | 7.013     |
| Random Forest                               | 6.050     |
| Gradient Boosting                           | 6.491     |
| **Gradient Boosting + Historical Features** | **5.831** |

Adding `route_median_duration` and `hour_route_median` as engineered features (computed only on training data, to avoid leakage) closed most of the gap to the baseline while retaining the flexibility to combine this signal with other features.

**Note on preprocessing:** `HistGradientBoostingRegressor` does not accept sparse input, so a separate `OrdinalEncoder`-based preprocessing pipeline was used for all tree-based models (vs. `OneHotEncoder` for linear models).

---

## Day 5 — Leakage Audit, Error Analysis & Explainability

### Leakage Experiment: Safe vs Oracle Model
| Model                                              | MAE   |
| -------------------------------------------------- | ----- |
| Safe Model (deployment-safe features only)         | 5.831 |
| Oracle Model (+ fare, tip, distance, total_amount) | 2.300 |

**Oracle outperforms Safe by 3.53 minutes.** This confirms that fare/tip/distance carry strong signal about trip duration, but they cannot be used in production because they are not known before or during the trip — only after it completes. This experiment validates the leakage-prevention approach used throughout the project.

### Feature Importance (Permutation Importance, Champion Model)
| Feature                 | Importance       |
| ----------------------- | ---------------- |
| `hour_route_median`     | 1.261 (dominant) |
| `pickup_dayofweek`      | 0.046            |
| `route_median_duration` | 0.010            |
| `is_airport_route`      | 0.005            |
| `pickup_hour`           | 0.005            |

The historical hour+route median dominates feature importance, confirming it captures most of the predictable signal. Remaining features contribute smaller, complementary adjustments.

### Error Analysis
- **By hour:** Error is lowest overnight (~4 min, hours 0–3) and highest during peak commute hours (~7 min, 7–8 AM and 3–5 PM), consistent with traffic-driven variability.
- **By borough:** Manhattan has the lowest error (5.14 min); Staten Island shows an extreme MAE (148 min), but this is a sample-size artifact — only **1 trip** from Staten Island appeared in the test set (a 162.5-minute outlier trip), not a systematic model failure.
- **Airport vs non-airport:** Airport trips have roughly double the error of non-airport trips (10.25 vs 5.20 min), reflecting longer and more variable trip lengths.

---

## Champion Model

**Gradient Boosting Regressor + Historical Route/Hour Features**
- Validation MAE: **5.831 minutes**
- Strengths: Best among all trained ML models; combines historical route/hour signal with contextual features (time, geography); more generalizable to unseen route/hour combinations than a pure lookup-table baseline.
- Limitation: Does not beat the raw Hour+Route median baseline (4.19 min) on this sample. The baseline's advantage comes from being a direct memorization of historical medians, which works well only when the exact route+hour combination is well-represented in history — a risk for rare or new routes in production.

---

## Limitations & Future Work
- **Hyperparameter tuning** was not formally performed (e.g., RandomizedSearchCV, Optuna) — default/lightly-tuned parameters were used due to time constraints. This is a recommended next step to close the gap with the baseline further.
- **SHAP analysis** was not completed; permutation importance was used instead as a faster alternative.
- **Log-target comparison** (training on log-transformed duration vs raw) was not formally benchmarked.
- **Single-month data** (January 2023, 500K sample) was used rather than the full 6-month, 1M+ row recommended dataset, due to development-time constraints.
- **Staten Island / low-volume boroughs** are underrepresented in this sample; error metrics for these segments should be treated with caution until more data is included.

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

## Summary Table — All Models
| Model                                                  | MAE (minutes) |
| ------------------------------------------------------ | ------------- |
| Baseline (Hour+Route Median)                           | 4.186         |
| **Gradient Boosting + Historical Features (Champion)** | **5.831**     |
| Random Forest                                          | 6.050         |
| Gradient Boosting                                      | 6.491         |
| Decision Tree                                          | 7.013         |
| Ridge                                                  | 7.262         |
| Linear Regression                                      | 7.264         |
| Elastic Net                                            | 7.593         |
| Lasso                                                  | 7.596         |
| Oracle Model (leakage, not deployable)                 | 2.300         |