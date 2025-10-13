"""
Qualification
"""

from dataclasses import dataclass
from datetime import date

@dataclass
class Qualification:
    """
    Qualification
    """

    name: str
    date_awarded: date
    # Optional fields
    reference: str | None = None
    verification_url: str | None = None
