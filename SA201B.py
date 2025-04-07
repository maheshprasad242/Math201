import math
import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(-3, 2, 400)
y_vals = np.exp(x_vals) + x_vals**2 - 4

plt.axhline(0, color='gray', linestyle='--')
plt.plot(x_vals, y_vals, label='f(x) = e^x + x^2 - 4')
plt.scatter([-1.841405], [0], color='red', label='Root ≈ -1.841405')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x)')
plt.legend()
plt.grid(True)
plt.show()
