"""Utility functions."""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to the starship test."


def calculate(a: float, b: float, operation: str = "add") -> float:
    """Perform basic arithmetic."""
    ops = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else float("inf"),
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return ops[operation](a, b)


def validate_input(data: str) -> str:
    """Sanitize and validate input."""
    if not data or not data.strip():
        raise ValueError("Input cannot be empty")
    return data.strip()
