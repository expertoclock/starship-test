"""Tests for utility functions."""
from src.utils import greet, calculate, validate_input
import pytest


def test_greet():
    assert "Starship" in greet("Starship")


def test_calculate_add():
    assert calculate(2, 3, "add") == 5


def test_calculate_subtract():
    assert calculate(10, 4, "subtract") == 6


def test_calculate_multiply():
    assert calculate(6, 7, "multiply") == 42


def test_calculate_divide_by_zero():
    assert calculate(1, 0, "divide") == float("inf")


def test_validate_input():
    assert validate_input("  hello  ") == "hello"


def test_validate_input_empty():
    with pytest.raises(ValueError):
        validate_input("")
