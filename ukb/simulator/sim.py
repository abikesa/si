# simulate.py
from lifelines import AalenJohansenFitter
import numpy as np
import pandas as pd

# -------------------------------
# CONFIGURATION
# -------------------------------
np.random.seed(42)
n_patients = 1000
censor_limit = 5.0  # Max follow-up in years

# -------------------------------
# SIMULATE PATIENT CHARACTERISTICS
# -------------------------------
age = np.random.normal(loc=65, scale=10, size=n_patients)
sex = np.random.choice(['Male', 'Female'], size=n_patients)
creatinine = np.random.exponential(scale=1.2, size=n_patients) + 0.5
black_race = np.random.choice([0, 1], size=n_patients, p=[0.7, 0.3])
diabetes = np.random.choice([0, 1], size=n_patients, p=[0.6, 0.4])
sex_male = (sex == 'Male').astype(int)

# -------------------------------
# SIMULATE COMPETING RISKS
# -------------------------------
X = np.column_stack([age, sex_male, creatinine, black_race, diabetes])

# Define true hazard coefficients
beta_death = np.array([0.03, 0.5, 0.4, 0.3, 0.2])
beta_tx    = np.array([-0.02, -0.4, -0.5, -0.2, -0.3])

# Base hazard rates
baseline_death = 0.005
baseline_tx = 0.007

# Compute hazard for each person
hazard_death = baseline_death * np.exp(np.dot(X, beta_death))
hazard_tx    = baseline_tx * np.exp(np.dot(X, beta_tx))

# Sample times to event
time_death = np.random.exponential(scale=1 / hazard_death)
time_tx    = np.random.exponential(scale=1 / hazard_tx)

# Competing risk logic
event_time = np.minimum(time_death, time_tx)
event_type = np.where(time_death < time_tx, 1, 2)  # 1 = death, 2 = transplant

# Censoring
censored = event_time > censor_limit
event_time[censored] = censor_limit
event_type[censored] = 0  # 0 = censored

# -------------------------------
# CREATE DATAFRAME
# -------------------------------
df = pd.DataFrame({
    'age': age.round(1),
    'sex': sex,
    'creatinine': creatinine.round(2),
    'black_race': black_race,
    'diabetes': diabetes,
    'time': event_time.round(2),
    'event': event_type
})

# -------------------------------
# EXPORT
# -------------------------------
df.to_csv('simulated_clinical_data.csv', index=False)
print("✅ Simulated dataset saved as 'simulated_clinical_data.csv'")
