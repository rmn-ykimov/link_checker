import pytest

from link_checker import LinkChecker


def test_validate_link():
    link_checker = LinkChecker()

    # test for invalid link
    with pytest.raises(Exception,
                       match='The string test is not a valid link.'):
        link_checker.validate_link('test')

    # test for valid link
    assert link_checker.validate_link('http://www.google.com') is True
