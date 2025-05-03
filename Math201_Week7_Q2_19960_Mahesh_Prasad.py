# MATH201 - Calculus-I
# Homework Assignment #7
# Mahesh Prasad (Student Id 19960)

import numpy as np
import matplotlib.pyplot as plt

def sin_function(x):
    return np.sin(x)

def line_function(x):
    return -(3 / (7 * np.pi)) * x

x_min = 0
x_max = 7 * np.pi / 6
y_min = -0.6
y_max = 1.1

num_points = 10000
x_random = np.random.uniform(x_min, x_max, num_points)
y_random = np.random.uniform(y_min, y_max, num_points)

points_under_sine_above_line = 0
for i in range(num_points):
    if y_random[i] < sin_function(x_random[i]) and y_random[i] > line_function(x_random[i]):
        points_under_sine_above_line += 1

total_area = (x_max - x_min) * (y_max - y_min)
estimated_area = (points_under_sine_above_line / num_points) * total_area

print(f"Estimated area using Monte Carlo simulation: {estimated_area}")

# Optional Visualization
x = np.linspace(0, 7 * np.pi / 6, 100)
y_sin = sin_function(x)
y_line = line_function(x)

plt.plot(x, y_sin, label='y = sin(x)')
plt.plot(x, y_line, label='y = -3/(7pi)x')
plt.scatter(x_random, y_random, s=1, color='gray', alpha=0.5, label='Random Points')

x_region = []
y_region = []
for i in range(num_points):
    if y_random[i] < sin_function(x_random[i]) and y_random[i] > line_function(x_random[i]):
        x_region.append(x_random[i])
        y_region.append(y_random[i])

plt.scatter(x_region, y_region, s=5, color='red', label='Points in Region')
plt.fill_between(x, y_sin, y_line, where=(y_sin > y_line), color='pink', alpha=0.3, label='Area')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area between y = sin(x) and y = -3/(7pi)x')
plt.xlim(0, 7 * np.pi / 6)
plt.ylim(y_min, y_max)
plt.grid(True)
plt.legend()
plt.show()
