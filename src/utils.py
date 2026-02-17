"""Utils."""

def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate(a: float, b: float, op: str = "add") -> float:
    ops = {"add": lambda x,y: x+y, "subtract": lambda x,y: x-y, "multiply": lambda x,y: x*y}
    return ops[op](a, b)

def validate_input(data: str) -> str:
    if not data or not data.strip(): raise ValueError("Empty")
    return data.strip()
