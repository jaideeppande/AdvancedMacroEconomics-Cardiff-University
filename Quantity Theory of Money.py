import numpy as np
import matplotlib.pyplot as plt

# Define parameters
time_periods = 30  # Number of time periods
shock_time = 5  # Time period where a shock occurs

# Initialize arrays for variables
p_t = np.zeros(time_periods)  # Price level deviation from normal
y_t = np.zeros(time_periods)  # Output deviation from normal
m_t = np.zeros(time_periods)  # Money supply deviation from normal

# Introduce a shock to money supply at t=5
m_t[shock_time] = 1.0  # Positive shock to money supply

# Simulate the Quantity Theory of Money relationship: m_t = p_t + y_t
for t in range(1, time_periods):
    # Assume some proportion of money supply affects price and output
    p_t[t] = 0.6 * m_t[t]  # 60% of money supply change affects prices
    y_t[t] = 0.4 * m_t[t]  # 40% of money supply change affects output

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(m_t, label="Money Supply Deviation ($m_t$)", color='black', linestyle='-')
plt.plot(p_t, label="Price Level Deviation ($p_t$)", color='red', linestyle='--')
plt.plot(y_t, label="Output Deviation ($y_t$)", color='blue', linestyle='-.')

# Labels and title
plt.xlabel("Time Periods")
plt.ylabel("Deviation from Normal")
plt.title("Quantity Theory of Money: Effect of Money Supply on Prices and Output")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
