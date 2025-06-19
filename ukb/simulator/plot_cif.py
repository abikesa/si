# plot_cifs_fixed.py

import pandas as pd
import matplotlib.pyplot as plt
# from lifelines import CumulativeIncidenceFitter
from lifelines import AalenJohansenFitter


# Load data
df = pd.read_csv("data/simulated_clinical_data.csv")

# Extract time and event type
T = df['time']
E = df['event']  # 0 = censored, 1 = death, 2 = transplant

# Initialize CIF
cif = AalenJohansenFitter()

# Plot
plt.figure(figsize=(10, 6))

# Fit and plot for each event type
for code, label, color in [(1, "Death", "crimson"), (2, "Transplant", "seagreen")]:
    cif.fit(T, E, event_of_interest=code, label=label)
    cif.plot(ci_show=False, color=color)

# Formatting
plt.title("Overlayed Cumulative Incidence Functions (Properly Modeled)")
plt.xlabel("Time (years)")
plt.ylabel("Cumulative Incidence")
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()
