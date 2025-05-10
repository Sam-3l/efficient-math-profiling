"""
🔧 Newton-Raphson Method Logic
To find the root of a function 
f(x), Newton-Raphson uses: 

🧩 Step-by-Step Custom Implementation (No NumPy)
"""

def newton_raphson(f, df, x0, tolerance=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero. No solution found.")
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new
    
    raise ValueError("Did not converge within max iterations")

# Example usage
if __name__ == "__main__":
    # Define the function and its derivative
    f = lambda x: x**2 - 2  # f(x) = x^2 - 2
    df = lambda x: 2*x      # f'(x) = 2x

    # Initial guess
    x0 = 1.0

    # Find the root
    root = newton_raphson(f, df, x0)
    print(f"Root found: {root}")


# Bisection vs Newton Raphson methods in number of steps taken to converge
def bisection(f, low, high, tolerance=1e-6, max_iter=100):
    steps = 0
    while steps < max_iter:
        mid = (low + high) / 2
        f_mid = f(mid)
        if abs(f_mid) < tolerance or abs(high - low) < tolerance:
            return mid, steps
        elif f(low) * f_mid < 0:
            high = mid
        else:
            low = mid
        steps += 1
    raise ValueError("Bisection did not converge")

def newton_raphson(f, df, x0, tolerance=1e-6, max_iter=100):
    x = x0
    steps = 0
    while steps < max_iter:
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tolerance:
            return x_new, steps
        x = x_new
        steps += 1
    raise ValueError("Newton-Raphson did not converge")

def compare_methods(f, df, x0, low, high):
    root_bisect, steps_bisect = bisection(f, low, high)
    root_newton, steps_newton = newton_raphson(f, df, x0)
    
    print(f"Bisection: Root = {root_bisect:.6f}, Steps = {steps_bisect}")
    print(f"Newton-Raphson: Root = {root_newton:.6f}, Steps = {steps_newton}")

# Example usage
if __name__ == "__main__":
    # Define the function and its derivative
    f = lambda x: x**2 - 2  # f(x) = x^2 - 2
    df = lambda x: 2*x      # f'(x) = 2x

    # Initial guess for Newton-Raphson
    x0 = 1.0

    # Interval for Bisection
    low, high = 0, 2

    # Compare methods
    compare_methods(f, df, x0, low, high)

# This code compares the Bisection and Newton-Raphson methods in terms of the number of steps taken to converge to the root of the function f(x) = x^2 - 2.
# The Bisection method is slower but more robust, while the Newton-Raphson method is faster but requires a good initial guess and a non-zero derivative.