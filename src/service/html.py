"""
HTML Service
"""

from dataclasses import asdict
import logging
from jinja2 import Template
from src.model.cv_definition import CvDefinition
from src.util.date import get_display_date_range

class HtmlService:
    """
    HTML Service
    """

    def __init__(
        self,
        cv_definition: CvDefinition,
        template_string: str
    ):
        self.cv_definition = cv_definition
        self.template_string = template_string


    def get_template(self) -> Template:
        """
        Retrieve template
        """

        return Template(source=self.template_string)


    def get_html(self) -> str:
        """
        Get HTML Output from template
        """

        logging.info('Generating HTML string from Jinja template')
        template = self.get_template()
        # Add custom functions
        template.globals['date_range'] = get_display_date_range

        html = template.render(asdict(self.cv_definition))

        return html
