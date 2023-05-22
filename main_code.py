import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the control limits
def calculate_control_limits(data, num_std):
    mean = np.mean(data)
    std = np.std(data)
    upper_limit = mean + (num_std * std)
    lower_limit = mean - (num_std * std)
    return upper_limit, lower_limit

# Generate sample data (number of items scanned per hour)
data = np.random.poisson(lam=200, size=1000)  # Using Poisson distribution for demonstration
data = data / 60  # Convert to rate per minute

# Convert the data to rate per hour
data = data * 60

# Calculate control limits (e.g., ±3 standard deviations)
num_std = 3
upper_limit, lower_limit = calculate_control_limits(data, num_std)

# Calculate the mean
mean = np.mean(data)

std = np.std(data)

print(f"The standard deviation of the data is: {std}")

print(f"The mean rate of items scanned per hour is: {mean}")

# Plot the control chart
plt.plot(data, 'bo-', label='Rate of Items Scanned')
plt.axhline(upper_limit, color='r', linestyle='--', label='Upper Control Limit')
plt.axhline(lower_limit, color='r', linestyle='--', label='Lower Control Limit')
plt.xlabel('Time Interval')
plt.ylabel('Rate of Items Scanned (per hour)')
plt.title('Control Chart')
plt.legend(loc='best')
plt.show()

# Check for outliers
outliers = [x for x in data if x > upper_limit or x < lower_limit]
if outliers:
    print(f"Outliers detected: {outliers}")
else:
    print("No outliers detected.")
