"""
Organisation
"""

from dataclasses import dataclass

@dataclass
class Organisation:
    """
    Organisation data class
    """

    # Required fields
    name: str
    logo_uri: str
    # Optional fields
    industry: str | None = None
