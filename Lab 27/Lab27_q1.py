# (1) Enzyme Activity vs Temperature

import numpy as np
import matplotlib.pyplot as plt

temps = np.arange(20, 71, 5)

activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])

# Find optimum temperature
optimum = temps[np.argmax(activity)]

# Plot
fig, ax = plt.subplots()

ax.plot(temps, activity, marker='o', linestyle='-', color='blue',
        label='Enzyme Activity')

# Mark optimum temperature
ax.axvline(optimum, color='red', linestyle='--',
           label=f'Optimum = {optimum}°C')

# Annotate peak
ax.annotate(
    f'Peak at {optimum}°C',
    xy=(optimum, max(activity)),
    xytext=(optimum + 5, max(activity) - 15),
    arrowprops=dict(arrowstyle='->', color='red')
)

ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Relative Activity')
ax.set_title('Enzyme Activity vs Temperature')

ax.legend()
ax.grid(True)

plt.show()

print("Optimum temperature:", optimum, "°C")
