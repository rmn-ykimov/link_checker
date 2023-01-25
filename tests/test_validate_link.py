import pytest

# from ..tests.helpers.helpers import raise_exception
from test_data import urls

@pytest.mark.parametrize("link, expected", [
    (urls['valid_https_link_example_com'], True),
    # Test valid https link
    (urls['valid_http_link_example_com'], True),
    # Test valid http link
    (urls['empty_link'], Exception("The string {} is not a valid link.".format(''))),
    # Test empty link
    (urls['invalid_link'],
     Exception("The string {} is not a valid link.".format('invalid_link'))),
    # Test invalid link
    (urls['invalid_link_scheme'], Exception(f"The link {urls['invalid_link_scheme']} is not a valid http or "
                                        "https protocol link."))
,
    # Test invalid link scheme
    (urls['url_with_port_number'], True),
    # Test url with port number
    (urls['url_with_path_and_query'], True),
    # Test url with path and query
    (urls['url_with_fragment'], True),
    # Test url with fragment
    (urls['url_with_encoded_spaces'], True),
    # Test url with encoded spaces
    (urls['url_with_path_query_and_fragment'], True),
    # Test url with path, query and fragment
    (urls['url_with_IPV6_and_port'], True),  # Test url with IPv6 and port number
    (urls['url_with_IPV6'], True),  # Test url with IPv6
    (urls['url_with_query'], True),  # Test url with query
    (urls['url_with_path'], True)  # Test url with path
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
