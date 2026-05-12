import pytest

# Import functions from the main component
from shift_validator import (
    calculate_shift_hours,
    validate_shift,
    calculate_total_hours,
    is_overtime
)


# Test a normal valid shift
def test_valid_shift():
    assert validate_shift("09:00", "17:00") is True


# Test a shift exceeding maximum allowed hours
def test_invalid_shift_hours():
    assert validate_shift("08:00", "23:00") is False


# Test invalid time order
def test_invalid_time_order():
    with pytest.raises(ValueError):
        calculate_shift_hours("18:00", "09:00")


# Test total hour calculation across shifts
def test_total_hours():

    shifts = [
        ("09:00", "17:00"),
        ("10:00", "14:00")
    ]

    assert calculate_total_hours(shifts) == 12


# Test overtime detection logic
def test_overtime_detection():
    assert is_overtime(45) is True


# Additional successful test cases

def test_short_shift():
    assert validate_shift("09:00", "12:00") is True


def test_exact_max_shift():
    assert validate_shift("08:00", "20:00") is True


def test_overtime_false():
    assert is_overtime(30) is False


def test_single_shift_total():
    shifts = [("09:00", "17:00")]
    assert calculate_total_hours(shifts) == 8


def test_two_hour_shift():
    assert calculate_shift_hours("10:00", "12:00") == 2


def test_five_hour_shift():
    assert calculate_shift_hours("09:00", "14:00") == 5


def test_night_shift_invalid():
    with pytest.raises(ValueError):
        calculate_shift_hours("22:00", "06:00")


def test_zero_hour_shift():
    with pytest.raises(ValueError):
        calculate_shift_hours("10:00", "10:00")


def test_large_total_hours():

    shifts = [
        ("08:00", "16:00"),
        ("09:00", "17:00")
    ]

    assert calculate_total_hours(shifts) == 16


def test_boundary_overtime():
    assert is_overtime(30) is True


