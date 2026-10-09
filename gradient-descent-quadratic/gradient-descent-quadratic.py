def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here

    for _ in range(steps):
        x0= x0 - lr*(a*2*x0+ b)
    return x0
    pass