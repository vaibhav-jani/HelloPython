"""
Examples demonstrating Python's datetime functionality.
This module shows various ways to work with dates and times in Python.
"""

from datetime import datetime, date, time, timedelta
import calendar
import pytz
from typing import List, Tuple


def basic_datetime_examples() -> None:
    """Demonstrate basic datetime operations."""
    print("\n=== Basic DateTime Examples ===")

    # Current date and time
    now = datetime.now()
    print(f"Current date and time: {now}")
    print(f"Current date: {now.date()}")
    print(f"Current time: {now.time()}")

    # Creating specific dates and times
    specific_date = date(2024, 3, 29)
    specific_time = time(14, 30, 0)
    specific_datetime = datetime(2024, 3, 29, 14, 30, 0)

    print(f"\nSpecific date: {specific_date}")
    print(f"Specific time: {specific_time}")
    print(f"Specific datetime: {specific_datetime}")


def datetime_formatting() -> None:
    """Show different ways to format dates and times."""
    print("\n=== DateTime Formatting ===")

    now = datetime.now()

    # Common format strings
    formats = {
        "Full date": "%Y-%m-%d",
        "Full time": "%H:%M:%S",
        "Date and time": "%Y-%m-%d %H:%M:%S",
        "Short date": "%d/%m/%Y",
        "12-hour time": "%I:%M %p",
        "Day name": "%A",
        "Month name": "%B",
        "Week number": "%W",
        "Day of year": "%j"
    }

    for description, fmt in formats.items():
        print(f"{description}: {now.strftime(fmt)}")


def datetime_arithmetic() -> None:
    """Demonstrate datetime arithmetic operations."""
    print("\n=== DateTime Arithmetic ===")

    now = datetime.now()

    # Adding/subtracting days
    tomorrow = now + timedelta(days=1)
    yesterday = now - timedelta(days=1)
    print(f"Tomorrow: {tomorrow}")
    print(f"Yesterday: {yesterday}")

    # Adding/subtracting hours
    in_3_hours = now + timedelta(hours=3)
    print(f"In 3 hours: {in_3_hours}")

    # Adding/subtracting weeks
    in_2_weeks = now + timedelta(weeks=2)
    print(f"In 2 weeks: {in_2_weeks}")

    # Difference between dates
    future_date = datetime(2025, 1, 1)
    days_until = (future_date - now).days
    print(f"Days until 2025: {days_until}")


def timezone_examples() -> None:
    """Show how to work with timezones."""
    print("\n=== Timezone Examples ===")

    # Current time in different timezones
    timezones = [
        "UTC",
        "America/New_York",
        "Europe/London",
        "Asia/Tokyo",
        "Australia/Sydney"
    ]

    for tz_name in timezones:
        tz = pytz.timezone(tz_name)
        local_time = datetime.now(tz)
        print(f"{tz_name}: {local_time}")


def calendar_examples() -> None:
    """Demonstrate calendar-related operations."""
    print("\n=== Calendar Examples ===")

    # Get current year and month
    now = datetime.now()
    year = now.year
    month = now.month

    # Print calendar for current month
    print(f"\nCalendar for {calendar.month_name[month]} {year}:")
    print(calendar.month(year, month))

    # Check if year is leap year
    is_leap = calendar.isleap(year)
    print(f"\nIs {year} a leap year? {is_leap}")

    # Get number of days in month
    days_in_month = calendar.monthrange(year, month)[1]
    print(f"Days in current month: {days_in_month}")


def date_validation() -> None:
    """Show how to validate dates."""
    print("\n=== Date Validation Examples ===")

    def is_valid_date(date_str: str) -> bool:
        """Check if a date string is valid."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    # Test some dates
    test_dates = [
        "2024-03-29",  # Valid
        "2024-13-29",  # Invalid month
        "2024-03-32",  # Invalid day
        "2024-02-30",  # Invalid for February
        "2024-03-29T14:30:00"  # Wrong format
    ]

    for date_str in test_dates:
        print(f"{date_str}: {'Valid' if is_valid_date(date_str) else 'Invalid'}")


def main() -> None:
    """Run all datetime examples."""
    print("Python DateTime Examples")
    print("=" * 50)

    basic_datetime_examples()
    datetime_formatting()
    datetime_arithmetic()
    timezone_examples()
    calendar_examples()
    date_validation()


if __name__ == "__main__":
    main()
