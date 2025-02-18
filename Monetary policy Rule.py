import numpy as np
import matplotlib.pyplot as plt

# Define parameters
time_periods = 30  # Number of time periods
mu = 0.7  # Reaction coefficient (how much the central bank responds to past output)
np.random.seed(42)  # For reproducibility

# Initialize arrays for variables
y_t = np.zeros(time_periods)  # Output deviation from normal
m_t = np.zeros(time_periods)  # Money supply deviation from normal
epsilon_t = np.random.normal(0, 0.2, time_periods)  # Random monetary shocks (normally distributed)

# Introduce an initial shock to output at t=5
y_t[5] = 1.0  

# Simulate the monetary policy rule: m_t = mu * y_t-1 + epsilon_t
for t in range(1, time_periods):
    m_t[t] = mu * y_t[t-1] + epsilon_t[t]  # Central bank response to past output deviation

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(m_t, label="Money Supply Deviation ($m_t$)", color='black', linestyle='-')
plt.plot(y_t, label="Output Deviation ($y_t$)", color='blue', linestyle='--')
plt.plot(epsilon_t, label="Random Monetary Shock ($\epsilon_t$)", color='red', linestyle=':')

# Labels and title
plt.xlabel("Time Periods")
plt.ylabel("Deviation from Normal")
plt.title("Monetary Policy Rule: Central Bank Response to Past Output and Shocks")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
