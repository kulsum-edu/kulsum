
import streamlit as st
import matplotlib.pyplot as plt

# Title
st.title("🌱 EV Impact: CO₂ Reduction in Thane by Replacing 2-Wheelers")

# Description
st.write("""
This simple app calculates and visualizes the reduction in annual CO₂ emissions
if a certain percentage of petrol-based 2-wheelers in Maharashtra (Thane region) 
are replaced with electric vehicles (EVs).
""")

# Raw data
total_2w_2023 = 31590000  # Total two-wheelers in 2023
emission_petrol = 0.72    # tons CO2 per petrol 2-wheeler/year
emission_ev = 0.10        # tons CO2 per EV 2-wheeler/year

# User input
ev_percent = st.slider("Select EV Replacement %", 0, 100, 20)
ev_fraction = ev_percent / 100
petrol_fraction = 1 - ev_fraction

# Calculate emissions
years = list(range(2025, 2035))
emissions = []

for y in years:
    total_emission = (total_2w_2023 * petrol_fraction * emission_petrol) +                      (total_2w_2023 * ev_fraction * emission_ev)
    emissions.append(round(total_emission / 1_000_000, 2))  # in million tons

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, emissions, marker='o', color='green')
ax.set_title(f"CO₂ Emissions with {ev_percent}% EV Replacement")
ax.set_xlabel("Year")
ax.set_ylabel("Emissions (Million Tons of CO₂)")
ax.grid(True)

# Show plot
st.pyplot(fig)

# CO2 saved display
emission_if_all_petrol = round((total_2w_2023 * emission_petrol) / 1_000_000, 2)
emission_now = emissions[0]
co2_saved = round(emission_if_all_petrol - emission_now, 2)

st.success(f"💡 Estimated CO₂ Saved per Year: {co2_saved} Million Tons")
