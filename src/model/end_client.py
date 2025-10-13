"""
End client
"""

from dataclasses import dataclass
from datetime import date
from src.model.project import Project
from src.model.organisation import Organisation

@dataclass
class EndClient:
    """
    End client data class
    """
    # Required fields
    organisation: Organisation
    # Optional fields
    projects: list[Project] | None = None
    summary: str | None = None
    details: list[str] | None = None
    role: str | None = None
    start_date: date | None = None
    end_date: date | None = None
