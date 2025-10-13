"""
Awarding Body
"""

from dataclasses import dataclass
from src.model.qualification import Qualification

@dataclass
class AwardingBody:
    """
    Awarding Body
    """

    # Required fields
    name: str
    qualifications: list[Qualification]
    # Optional fields
    column: int = 1
    logo_uri: str | None = None
    verification_url_prefix: str | None = None
