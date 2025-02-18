import numpy as np
import matplotlib.pyplot as plt

# Define parameters
beta = 0.8  # Sensitivity of output to price deviations
time_periods = 30  # Number of time periods to simulate

# Initialize arrays for variables
p_t = np.zeros(time_periods)  # Price level deviation
y_t = np.zeros(time_periods)  # Output deviation
E_t1_p_t = np.zeros(time_periods)  # Expected price at t based on t-1
E_t2_p_t = np.zeros(time_periods)  # Expected price at t based on t-2

# Introduce a shock to price levels at t=5
p_t[5] = 1.0  

# Simulate the model dynamics
for t in range(2, time_periods):
    # Forming expectations as a simple lag (adaptive expectations assumption)
    E_t1_p_t[t] = p_t[t-1]
    E_t2_p_t[t] = p_t[t-2]
    
    # Compute output deviation using the given equation
    y_t[t] = beta * (p_t[t] - 0.5 * (E_t1_p_t[t] + E_t2_p_t[t]))

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(y_t, label="Output Deviation ($y_t$)", color='blue', linestyle='-')
plt.plot(p_t, label="Price Level Deviation ($p_t$)", color='red', linestyle='--')
plt.plot(E_t1_p_t, label="Expected Price Level ($E_{t-1} p_t$)", color='green', linestyle='-.')
plt.plot(E_t2_p_t, label="Expected Price Level ($E_{t-2} p_t$)", color='purple', linestyle=':')

# Labels and title
plt.xlabel("Time Periods")
plt.ylabel("Deviation from Normal")
plt.title("Dynamics of Output and Price Expectations (Lucas Critique)")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
