import pytest

from ..tests.helpers.helpers import raise_exception

valid_https_link = 'https://www.example.com'
valid_http_link = 'http://www.example.com'
empty_link = ''
invalid_link = 'invalid_link'
invalid_link_scheme = 'ftp://www.example.com'
url_with_credentials = 'ftp://www.example.com'
url_with_port_number = 'http://www.example.com:8080'
url_with_path_and_query = 'http://www.example.com/path?query=value'
url_with_fragment = 'http://www.example.com/path#fragment'
url_with_encoded_spaces = 'http://www.example.com/path%20with%20spaces'
url_with_path_query_and_fragment = 'http://www.example.com/path?query=value#fragment'
url_with_IPV6 = 'http://[::1]'
url_with_IPV6_and_port = 'http://[::1]:8080'
url_with_query = 'http://www.example.com?query=value'
url_with_path = 'http://www.example.com:8080/path'


@pytest.mark.parametrize("link, expected", [
    (valid_https_link, True),
    # Test valid https link
    (valid_http_link, True),
    # Test valid http link
    (empty_link, Exception("The string {} is not a valid link.".format(''))),
    # Test empty link
    (invalid_link,
     Exception("The string {} is not a valid link.".format('invalid_link'))),
    # Test invalid link
    (invalid_link_scheme, Exception("The link {} is not a valid http or "
                                    "https protocol link.".format(
        'ftp://www.example.com'))),
    # Test invalid link scheme
    (url_with_credentials, True),
    # Test url with credentials
    (url_with_port_number, True),
    # Test url with port number
    (url_with_path_and_query, True),
    # Test url with path and query
    (url_with_fragment, True),
    # Test url with fragment
    (url_with_encoded_spaces, True),
    # Test url with encoded spaces
    (url_with_path_query_and_fragment, True),
    # Test url with path, query and fragment
    (url_with_IPV6_and_port, True),  # Test url with IPv6 and port number
    (url_with_IPV6, True),  # Test url with IPv6
    (url_with_query, True),  # Test url with query
    (url_with_path, True)  # Test url with path
])
def test_validate_link(link_checker, link, expected):
    """
    Test the validate_link method of the LinkChecker class
    :param link_checker: instance of the LinkChecker class
    :param link: The link to be validated
    :param expected: The expected result of the validation
    """
    if isinstance(expected, Exception):
        # Use the assertRaises method from pytest to check if the exception
        # is raised
        with pytest.raises(expected.__class__) as excinfo:
            result = link_checker.validate_link(link)
        # Assert that the message of the raised exception is the same as the
        # expected message
        assert str(excinfo.value) == str(expected)

    else:
        result = link_checker.validate_link(link)
        assert result == expected
