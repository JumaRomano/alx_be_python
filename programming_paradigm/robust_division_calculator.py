# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Safely divide two numbers, handling errors."""
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom}"
    except ValueError:
        return "Error: Please enter numeric values only."
