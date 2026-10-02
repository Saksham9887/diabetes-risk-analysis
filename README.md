# Diabetes Risk Factor Analysis

Exploratory data analysis on the Pima Indians Diabetes dataset (768 patients, 8 health
metrics) to identify which factors are most strongly associated with diabetes onset.

## Key Findings
- **Glucose level was the strongest single predictor** (correlation 0.47 with diabetes
  outcome) — diabetic patients had an average glucose of 141 vs 110 for non-diabetic
  patients, a 28% difference.
- **BMI and age were secondary but meaningful factors** (correlations 0.29 and 0.24):
  diabetic patients averaged 16% higher BMI and were on average 6 years older.
- **Pregnancies showed a moderate correlation** (0.22), consistent with known
  gestational diabetes risk patterns.
- **Blood pressure and skin thickness showed the weakest correlation** with outcome
  (both under 0.08), suggesting they're poor standalone predictors in this dataset.

## Data Quality Note
Several features (Glucose, BMI, BloodPressure, SkinThickness, Insulin) contain zero
values that are not biologically possible and likely represent missing data encoded
as 0 rather than NaN — a known characteristic of this dataset. A pandas `isnull()`
check alone does not catch this, so any production use of this data would need
explicit zero-as-missing handling before modeling.

## Tools
Python, Pandas, Matplotlib

## Run it
    pip install pandas matplotlib
    python main.py