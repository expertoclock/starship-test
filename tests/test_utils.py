"""Tests."""
from src.utils import greet, calculate, validate_input
import pytest

def test_greet(): assert "Starship" in greet("Starship")
def test_add(): assert calculate(2, 3) == 5
def test_mul(): assert calculate(6, 7, "multiply") == 42
def test_val(): assert validate_input("  hi  ") == "hi"
def test_val_empty():
    with pytest.raises(ValueError): validate_input("")
