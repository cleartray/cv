"""
An independent project is performed outside of formal employment with an employer.
"""

from dataclasses import dataclass
from datetime import date
from src.model.organisation import Organisation

@dataclass
class IndependentProject:
    """
    Role data class.
    """

    # Required fields
    organisation: Organisation
    # Optional fields
    role: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    summary: str | None = None
    details: list[str] | None = None
