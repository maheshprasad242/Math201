# MATH201 - Calculus-I
# Homework Assignment #7
# Mahesh Prasad (Student Id 19960)

import sympy

# Define the symbolic variable x
x = sympy.Symbol('x')

# Define the integrand
integrand = (1 + sympy.ln(x)) * sympy.sqrt(1 + (x * sympy.ln(x))**2)

# Define the limits of integration
lower_limit = 0.2
upper_limit = 1

# Calculate the definite integral
definite_integral = sympy.integrate(integrand, (x, lower_limit, upper_limit))

# Print the result
print(f"The definite integral of (1 + ln(x)) * sqrt(1 + (x*ln(x))^2) from 0.2 to 1 is approximately: {definite_integral.evalf()}")
