import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g_x = np.polyval(g_coeffs, x)
    h_x = np.polyval(h_coeffs, x)
    g_prime = np.polyval(np.polyder(g_coeffs), x)
    h_prime = np.polyval(np.polyder(h_coeffs), x)
    return ((g_prime * h_x) - (g_x * h_prime)) / (h_x ** 2)