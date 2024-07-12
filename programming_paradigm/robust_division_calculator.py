def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Cannot divide by zero."
    else:
        return f"The result of the division is {result}"