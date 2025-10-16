"""
CV Definition
"""

from dataclasses import dataclass
from enum import Enum
from src.model.awarding_body import AwardingBody
from src.model.employment import Employment
from src.model.independent_project import IndependentProject
from src.model.personal_details import PersonalDetails

class ExperienceLayout(str, Enum):
    """
    Experience layout options.
    """
    PROJECT = "project"
    SKILL = "skill"

@dataclass
class CvDefinition:
    """
    Define the required and optional fields in a CV.
    Used to generate an output CV Document
    """

    # Required fields
    personal_details: PersonalDetails
    profile: str
    employments: list[Employment]
    # Optional fields
    end_client_layout: str = ExperienceLayout.PROJECT
    employment_layout: str = ExperienceLayout.PROJECT
    independent_projects: list[IndependentProject] | None = None
    awarding_bodies: list[AwardingBody] | None = None
    skills: list[dict[str, str]] | None = None
