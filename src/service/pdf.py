"""
PDF Service
"""

from pathlib import Path
from jinja2 import Template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

class PdfService:
    """
    PDF Service
    """

    def __init__(
        self,
        output_path: Path,
        html: str,
        stylesheet_strings: list[str] | None,
    ):
        """
        Initialise PDF Service
        """
        self.output_path = output_path
        self.html = html
        self.font_config = FontConfiguration()
        self.stylesheet_strings = stylesheet_strings
        self.stylesheets: list[CSS] | None = None
        self.base_path = Path(__file__).parent.parent.parent.joinpath('input').absolute()


    def get_stylesheets(self):
        """
        Load all CSS files
        """
        output = []

        if not self.stylesheet_strings:
            return output

        for stylesheet_string in self.stylesheet_strings:
            template = Template(source=stylesheet_string)
            template_output = template.render({'base_path': self.base_path})
            output.append(CSS(string=template_output, font_config=self.font_config))

        return output


    def generate(self):
        """
        Generate a PDF
        """

        html = HTML(string=self.html, base_url=self.base_path)

        html.write_pdf(
            target=self.output_path,
            stylesheets=self.get_stylesheets(),
            font_config=self.font_config
        )
