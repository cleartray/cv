"""
A role is held while being employed. As part of a role, can be placed with multiple end-clients.
"""

from dataclasses import dataclass
from datetime import date
from src.model.end_client import EndClient
from src.model.project import Project

@dataclass
class Role:
    """
    Role data class.
    """

    # Required fields
    name: str
    # Optional fields
    projects: list[Project] | None = None
    end_clients: list[EndClient] | None = None
    summary: str | None = None
    start_date: date | None = None
    end_date: date | None = None
