"""
Date utilities
"""

from datetime import date

def get_display_date_range(start_date: date | None, end_date: date | None) -> str:
    """
    Given a start and end date, calculate the date range used for display purposes.
    examples:
        - Feb 2024 - Present
        - Feb 2024 - Nov 2025
    """
    output = ''
    if start_date:
        start = start_date.strftime('%b %Y')
        end = 'Present' if end_date is None else end_date.strftime('%b %Y')
        return f'{start} - {end}'
    return output
