"""
Employer
"""

from dataclasses import dataclass

@dataclass
class Employer:
    """
    Employer data class
    """

    # Required fields
    name: str
    logo_uri: str
    # Optional fields
    industry: str | None = None
    summary: str | None = None
