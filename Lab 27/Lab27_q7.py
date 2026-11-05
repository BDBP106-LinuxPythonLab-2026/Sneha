import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-10, 10, 1000)

# Standard deviations
sigmas = [1, 1.5, 2]

plt.figure(figsize=(10, 6))

# Plot Gaussian functions
for sigma in sigmas:

    g = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(
        -(x**2) / (2 * sigma**2)
    )

    plt.plot(x, g, label=f'Sigma = {sigma}')

plt.xlabel('x')
plt.ylabel('g(x)')

plt.title('Normalized Gaussian Functions')

plt.legend()
plt.grid(True)

plt.show()
