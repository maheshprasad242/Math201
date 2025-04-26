# Math 201 - Calculus-I
# Homework Assignment #6
# Mahesh Prasad (Student Id 19960)

import sympy as sp
import math

# Define variables
x = sp.symbols('x')

# Question 1 (a)
integral_a = sp.integrate(3 * sp.sqrt(x), (x, 4, 9))
print(f"Question 1 (a) : {integral_a}")

# Question 1 (b)
integral_b = sp.integrate(sp.ln(x), (x, 1, math.e))
print(f"Question 1 (b) : {integral_b}")

# Question 1 (c)
integral_c = sp.integrate(sp.acos(x), (x, 0, 1))
print(f"Question 1 (c) : {integral_c}")

# Question 1 (d)
integral_d = sp.integrate(sp.pi * sp.cos(sp.pi * x / 2), (x, -1, 1))
print(f"Question 1 (d) : {integral_d}")
