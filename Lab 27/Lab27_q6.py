import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 points
x = np.linspace(-20, 20, 1000)

# Calculate functions
f1 = np.log(1 / np.cos(x)**2)

f2 = np.log(1 / np.sin(x)**2)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(x, f1, label='f1(x) = ln(1/cos²x)', color='blue')

plt.plot(x, f2, label='f2(x) = ln(1/sin²x)', color='red')

plt.xlabel('x')
plt.ylabel('Function Value')

plt.title('Plot of f1(x) and f2(x)')

plt.ylim(-2, 10)

plt.legend()
plt.grid(True)

plt.show()
