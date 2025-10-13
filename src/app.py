"""
Build CVs
"""

import logging
import sys
from src.service.cv import CvService


def handler(event: dict, context: dict):
    """
    AWS Lambda function handler.
    """

    logging.debug(event)
    logging.debug(context)

    service = CvService(
        cv_definitions=event.get('cv_definitions'),
        template_string=event.get('template_string'),
        stylesheet_strings=event.get('stylesheet_strings'),
    )

    service.run()


# Invoke handler if running locally or directly
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    handler({}, {})
