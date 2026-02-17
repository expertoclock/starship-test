"""Main."""
from src.utils import greet, calculate

def main() -> None:
    print(greet("Starship"))
    print(f"2 + 3 = {calculate(2, 3)}")
    print(f"6 x 7 = {calculate(6, 7, \"multiply\")}")

if __name__ == "__main__":
    main()
