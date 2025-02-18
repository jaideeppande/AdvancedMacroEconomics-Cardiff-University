import numpy as np
import matplotlib.pyplot as plt

# Define unemployment rates
unemployment_rate = np.linspace(2, 10, 100)

# Define parameters for the Phillips Curve
natural_unemployment_rate = 5  # Natural rate of unemployment
initial_inflation = 2          # Initial inflation rate at natural unemployment
expected_inflation_shift = 3   # Increase in expected inflation

# Calculate initial Phillips Curve (SRPC1)
initial_phillips_curve = initial_inflation - 0.5 * (unemployment_rate - natural_unemployment_rate)

# Calculate shifted Phillips Curve (SRPC2) due to increased expected inflation
shifted_phillips_curve = (initial_inflation + expected_inflation_shift) - 0.5 * (unemployment_rate - natural_unemployment_rate)

# Plotting the Phillips Curves
plt.figure(figsize=(10, 6))
plt.plot(unemployment_rate, initial_phillips_curve, label='Initial SRPC', color='blue')
plt.plot(unemployment_rate, shifted_phillips_curve, label='Shifted SRPC', color='red', linestyle='--')

# Highlighting points A, B, and C
plt.scatter([natural_unemployment_rate], [initial_inflation], color='blue')  # Point A
plt.text(natural_unemployment_rate + 0.2, initial_inflation, 'A', fontsize=12, color='blue')

plt.scatter([natural_unemployment_rate - 1], [initial_inflation + 0.5], color='blue')  # Point B
plt.text(natural_unemployment_rate - 0.8, initial_inflation + 0.5, 'B', fontsize=12, color='blue')

plt.scatter([natural_unemployment_rate - 1], [initial_inflation + expected_inflation_shift + 0.5], color='red')  # Point C
plt.text(natural_unemployment_rate - 0.8, initial_inflation + expected_inflation_shift + 0.5, 'C', fontsize=12, color='red')

# Adding labels and title
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Inflation Rate (%)')
plt.title('Impact of Expected Inflation on the Phillips Curve')
plt.legend()
plt.grid(True)
plt.axvline(x=natural_unemployment_rate, color='gray', linestyle=':', linewidth=1)
plt.axhline(y=initial_inflation, color='gray', linestyle=':', linewidth=1)

# Show plot
plt.show()
