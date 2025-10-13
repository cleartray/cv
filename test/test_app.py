"""
Test app handler
"""

from src.app import handler

def test_app():
    """
    Verify app handler can execute with no inputs
    """

    assert handler(event={}, context={}) is None
