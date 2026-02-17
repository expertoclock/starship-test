"""Main application entry point."""
from src.utils import greet, calculate


def main() -> None:
    """Run the application."""
    print(greet("Starship"))
    print(f"2 + 3 = {calculate(2, 3, 'add')}")
    print(f"10 - 4 = {calculate(10, 4, 'subtract')}")
    print(f"6 * 7 = {calculate(6, 7, 'multiply')}")


if __name__ == "__main__":
    main()
