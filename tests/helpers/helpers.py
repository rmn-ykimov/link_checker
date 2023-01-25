def raise_exception(link, expected, result):
    """
    Raise an exception if the link is not valid.
    :param link: The link to be validated
    :param expected: The expected result of the validation
    :param result: The actual result of the validation
    """
    if isinstance(expected, Exception) and result != expected:
        raise expected
