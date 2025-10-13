"""
An employment object is a period of time with an employer.
An employer can span multiple end-clients with each end-client having multiple projects.
"""

from dataclasses import dataclass
from datetime import date
from src.model.organisation import Organisation
from src.model.role import Role


@dataclass
class Employment:
    """
    Employment block
    Promotions or moves to different roles with the same employer are tracked as roles
    """

    # Required fields
    organisation: Organisation
    # Optional fields
    role: str | None = None
    roles: list[Role] | None = None
    start_date: date | None = None
    end_date: date | None = None
    summary: str | None = None
    details: list[str] | None = None
