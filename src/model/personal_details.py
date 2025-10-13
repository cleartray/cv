"""
Personal Details
"""

from dataclasses import dataclass

@dataclass
class PersonalDetails:
    """
    Personal Details class
    """

    # Required fields
    name: str
    email: str
    phone: str
    title: str
    # Optional fields
    github_username: str | None = None
