import pytest

from ..link_checker import LinkChecker


# Use parametrize feature to test the function with different inputs
@pytest.mark.parametrize("link, expected_result", [
    ('test', False),  # test for invalid link
    ('http://www.google.com', True),  # test for valid http link
    ('ftp://www.google.com', False),  # test for invalid protocol
    ('www.google.com', False),  # test for missing scheme
    ('HTTP://WWW.GOOGLE.COM', True),  # test for case-insensitivity
])
def test_validate_link(link, expected_result):
    link_checker = LinkChecker()
    # check the exception message for invalid links
    if not expected_result:
        with pytest.raises(Exception,
                           match=f'The string {link} is not a valid link.'):
            link_checker.validate_link(link)
    # check the returned result for valid links
    else:
        assert link_checker.validate_link(
            link) == expected_result, f'Failed for link: {link}'


@pytest.mark.parametrize("link, timeout, expected_result", [
    ('http://www.google.com', 1, True),  # test with low timeout
    ('http://www.google.com', 10, True),  # test with high timeout
    ('http://nonexistent.example', 1, False),
    # test with unreachable link and low timeout
])
@pytest.mark.parametrize("link, timeout, expected_result", [
    ('http://www.google.com', 1, True),  # test with low timeout
    ('http://www.google.com', 10, True),  # test with high timeout
    ('http://www.google.com', None, True),  # test with None timeout
    ('http://www.google.com', 100000, True),  # test with large timeout
    ('http://nonexistent.example', 1, False),  # test with unreachable link
    # and low timeout
    ('', 1, False),  # test with empty link
    (None, 1, False),  # test with None link
    ('http://www.google.com', -1, False),  # test with negative timeout
])
def test_check_link_reachability(link, timeout, expected_result):
    # create an instance of the LinkChecker class
    link_checker = LinkChecker()
    # check the returned result for reachable links and unreachable links
    if timeout and timeout > 0:
        if expected_result:
            # assert the return value is as expected
            assert link_checker.check_link
