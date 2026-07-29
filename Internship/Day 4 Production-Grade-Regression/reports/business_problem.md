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