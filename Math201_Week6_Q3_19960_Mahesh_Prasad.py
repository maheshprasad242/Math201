# Math 201 - Calculus-I
# Homework Assignment #6
# Mahesh Prasad (Student Id 19960)

import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**3 - 5*x**2 + 30

# Define x values between 0 and 4
x = np.linspace(0, 4, 400)
y = f(x)

# Average value
f_avg = 58/3  # or approximately 19.33

# Plotting
plt.figure(figsize=(8,6))
plt.plot(x, y, label='f(x) = $x^3 - 5x^2 + 30$', color='blue')
plt.axhline(y=f_avg, color='red', linestyle='--', label=f'Average value ≈ {f_avg:.2f}')
plt.title('Elevation Function f(x) and its Average Value')
plt.xlabel('x (horizontal distance)')
plt.ylabel('f(x) (elevation)')
plt.legend()
plt.grid(True)
plt.show()
