import pytest

from ..link_checker import LinkChecker


@pytest.fixture
def link_checker():
    """
    Fixture that creates an instance of the LinkChecker class.
    """
    return LinkChecker()