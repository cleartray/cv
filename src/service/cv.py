"""
CV Service
"""

import logging
from pathlib import Path
from dacite import from_dict
from src.model.cv_definition import CvDefinition
from src.service.pdf import PdfService
from src.service.html import HtmlService

class CvService:
    """
    CV Service
    """

    def __init__(
        self,
        template_string: str | None = None,
        stylesheet_strings: list[str] | None = None,
        cv_definitions: list[CvDefinition | dict] | None = None
    ):
        """
        Initialise CV Service
        """

        # Set up output directory
        self.output_dir = Path(__file__).parent.parent.parent.joinpath('output')

        # Set up service inputs
        self.cv_definitions = cv_definitions
        self.stylesheet_strings = stylesheet_strings
        self.template_string = template_string


    def run(self):
        """
        Process all entries
        """

        if not self.cv_definitions:
            logging.info('No CV definitions provided, nothing to do.')
            return

        if not self.template_string:
            logging.info('No template provided, nothing to do.')
            return

        for cv_definition in self.cv_definitions:
            # Optionally convert from dict to dataclass
            if isinstance(cv_definition, dict):
                cv_definition = from_dict(CvDefinition, cv_definition)

            self.process_record(
                cv_definition=cv_definition,
                template_string=self.template_string,
                stylesheet_strings=self.stylesheet_strings
            )


    def process_record(
        self,
        cv_definition: CvDefinition,
        template_string: str,
        stylesheet_strings: list[str] | None = None,
    ):
        """
        Process a specific entry
        """

        # Generate HTML content
        html_service = HtmlService(
            cv_definition=cv_definition,
            template_string=template_string
        )
        html = html_service.get_html()

        # Set up PDF document with basic config
        filename = cv_definition.personal_details.name.lower().replace(' ', '-')
        output_path = self.output_dir.joinpath(f'{filename}.pdf')

        pdf = PdfService(
            html=html,
            stylesheet_strings=stylesheet_strings,
            output_path=output_path
        )

        pdf.generate()
