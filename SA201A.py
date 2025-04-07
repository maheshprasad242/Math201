import math

def f(x):
    return math.exp(x) + x**2 - 4

def f_prime(x):
    return math.exp(x) + 2*x

def newtons_method(x0, tolerance=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("Derivative is zero. Newton's method fails.")
        x_new = x - fx / fpx
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Did not converge")

root = newtons_method(-2)
print(f"Root approximated to six decimal places: {root:.6f}")

