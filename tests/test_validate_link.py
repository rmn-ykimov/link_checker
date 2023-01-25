import pytest


@pytest.mark.parametrize("link, expected", [
    ('https://www.example.com', True),
    # Test valid https link
    ('http://www.example.com', True),
    # Test valid http link
    ('', Exception("The string {} is not a valid link.".format(''))),
    # Test empty link
    ('invalid_link',
     Exception("The string {} is not a valid link.".format('invalid_link'))),
    # Test invalid link
    ('ftp://www.example.com', Exception(
        "The link {} is not a valid http or https protocol link.".format(
            'ftp://www.example.com'))),
    # Test invalid link scheme
    ('http://user:password@www.example.com', True),
    # Test url with credentials
    ('http://www.example.com:8080', True),
    # Test url with port number
    ('http://www.example.com/path?query=value', True),
    # Test url with path and query
    ('http://www.example.com/path#fragment', True),
    # Test url with fragment
    ('http://www.example.com/path%20with%20spaces', True),
    # Test url with encoded spaces
    ('http://www.example.com/path?query=value#fragment', True)
    # Test url with path, query and fragment
])
def test_validate_link(link_checker, link, expected):
    """
    Test the validate_link method of the LinkChecker class
    :param link_checker: instance of the LinkChecker class
    :param link: The link to be validated
    :param expected: The expected result of the validation
    """
    if isinstance(expected, Exception):
        with pytest.raises(Exception, match=str(expected)):
            link_checker.validate_link(link)
    else:
        assert link_checker.validate_link(link) == expected
