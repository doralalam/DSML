def addition(a, b):
    """Returns the sum of a and b."""
    return f"Adding two numbers using package {a+b}"

def subtraction(a, b):
    """Returns the difference of a and b."""
    return f"Subtracting two numbers using package {a-b}"

def multiplication(a, b):
    """Returns the product of a and b."""
    return f"Multiplying two numbers using package {a*b}"

def division(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return f"Dividing two numbers using package {a/b}"