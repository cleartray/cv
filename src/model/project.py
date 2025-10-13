"""
A project is worked on for an end-client
"""

from dataclasses import dataclass
from src.model.par import PAR
from src.model.star import STAR

@dataclass
class Project:
    """
    Project data class.
    """

    # Required fields
    name: str
    # Optional fields
    par: PAR | None = None
    star: STAR | None = None
    summary: str | None = None
