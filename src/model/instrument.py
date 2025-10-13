"""
An instrument is a tool, skill, technology or methodology used on a project.
"""

from dataclasses import dataclass

@dataclass
class Instrument:
    """
    Instrument data class.
    """

    # Required fields
    name: str
    # Optional fields
    summary: str | None = None
