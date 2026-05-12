from datetime import datetime

# Maximum allowed hours for a single shift
MAX_SHIFT_HOURS = 12

# Weekly overtime threshold
OVERTIME_LIMIT = 40


# Calculates the number of hours worked in a shift
def calculate_shift_hours(start, end):

    # Convert string times into datetime objects
    start_dt = datetime.strptime(start, "%H:%M")
    end_dt = datetime.strptime(end, "%H:%M")

    # Ensure the end time is after the start time
    if end_dt <= start_dt:
        raise ValueError("Shift end time must be after start time")

    # Calculate duration in hours
    duration = (end_dt - start_dt).seconds / 3600

    return duration


# Validates whether a shift is acceptable
def validate_shift(start, end):

    # Calculate total shift hours
    hours = calculate_shift_hours(start, end)

    # Reject shifts exceeding the maximum allowed hours
    if hours > MAX_SHIFT_HOURS:
        return False

    return True


# Calculates total hours worked across multiple shifts
def calculate_total_hours(shifts):

    total = 0

    # Loop through each shift tuple
    for start, end in shifts:
        total += calculate_shift_hours(start, end)

    return total


# Checks whether total hours exceed overtime threshold
def is_overtime(total_hours):

    return total_hours > OVERTIME_LIMIT