"""
Test CV Definition
"""

from datetime import date
from src.model.cv_definition import CvDefinition
from src.model.personal_details import PersonalDetails
from src.model.employment import Employment
from src.model.organisation import Organisation
from src.model.role import Role
from src.model.end_client import EndClient
from src.model.project import Project
from src.model.awarding_body import AwardingBody
from src.model.qualification import Qualification
from src.model.par import PAR


def test_cv_definition():
    """
    Test CV definition
    """

    cv = CvDefinition(
        personal_details=PersonalDetails(
            name="First Last",
            email="first.last@example.com",
            phone="+44 (0) 1234 567 890",
            title="Some role"
        ),
        profile="""

        """,
        awarding_bodies=[
            AwardingBody(
                name="Awarding Body 1",
                qualifications=[
                    Qualification(
                        name="Awarding Body Qualification 1",
                        date_awarded=date(year=2001, month=4, day=10)
                    ),
                    Qualification(
                        name="Awarding Body Qualification 2",
                        date_awarded=date(year=2003, month=2, day=24)
                    ),
                ],
            )
        ],
        employments=[
            Employment(
                organisation=Organisation(name="Employer 1", logo_uri="/employer-1-logo.svg"),
                roles=[
                    Role(
                        name="Role 1",
                        summary="Summary of role 1 held with employer 1",
                        end_clients=[
                            EndClient(
                                organisation=Organisation(
                                    name="End client 1",
                                    logo_uri="/end-client-1-logo.svg",
                                ),
                                start_date=date(year=2022, month=1, day=3),
                                summary="Summary of work completed for end client 1",
                                projects=[
                                    Project(
                                        name="Project 1",
                                        summary="""
                                            Summary of work completed within Project 1,
                                            written in PAR format
                                        """,
                                        par=PAR(
                                            problem="A convoluted and complex problem",
                                            action="Used methods and tools to resolve problem",
                                            result="Reduced complexity by 30%",
                                        ),
                                    ),
                                    Project(
                                        name="Project 2",
                                        summary="""
                                            Summary of work completed within Project 2, written in
                                            PAR format
                                        """,
                                        par=PAR(
                                            problem="Another convoluted and complex problem",
                                            action="""
                                                Used agile methods and technical tools to solve the
                                                problems faced by the end-client.
                                            """,
                                            result="Increase productivity by 15%",
                                        ),
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ],
    )

    assert cv.employments[0].roles[0].end_clients[0].projects[0].name == 'Project 1'
