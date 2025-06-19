import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# Load the simulated dataset
df = pd.read_csv("data/simulated_clinical_data.csv")

# Initialize KaplanMeierFitter instances for each event type
kmf_death = KaplanMeierFitter()
kmf_tx = KaplanMeierFitter()

# Define time and event
T = df['time']
E = df['event']

# CIF = 1 - KM curve for each event type (non-parametric approximation)

# Death CIF
death_mask = (E == 1)
kmf_death.fit(T, event_observed=death_mask, label='Death')

# Transplant CIF
tx_mask = (E == 2)
kmf_tx.fit(T, event_observed=tx_mask, label='Transplant')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(kmf_death.survival_function_.index,
         1 - kmf_death.survival_function_["Death"], label='CIF - Death', color='red')
plt.plot(kmf_tx.survival_function_.index,
         1 - kmf_tx.survival_function_["Transplant"], label='CIF - Transplant', color='green')

plt.title("Overlayed Cumulative Incidence Functions")
plt.xlabel("Time (years)")
plt.ylabel("Cumulative Incidence")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

