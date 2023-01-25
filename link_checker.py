"""
This module contains a class `LinkChecker` that is used for validating links,
checking their reachability, and checking available methods on them.
It uses the requests library to make HTTP requests and the urllib.parse module
to parse URLs.
"""

import logging
from urllib.parse import urlparse
import requests


logger = logging.getLogger()
logger.setLevel(logging.WARNING)


class LinkChecker:
    """
    Class to validate links and check available methods on them.
    """

    def __init__(self):
        self.methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT',
                        'OPTIONS', 'TRACE', 'PATCH']

    def validate_link(self, link: str) -> bool:
        """
        Validate if the provided link is a valid URL.
        :param link: The link to be validated.
        :return: True if the link is valid, False otherwise.
        """
        parsed_url = urlparse(link)
        # check if the link is valid or not
        if not parsed_url.scheme or not parsed_url.netloc:
            raise Exception(f"The string {link} is not a valid link.")
        if parsed_url.scheme not in ['http', 'https']:
            raise Exception(f"The link {link} is not a valid http or https "
                            f"protocol link.")
        return True

    def check_link_reachability(self, link: str, timeout: int = 5) -> bool:
        """
        Check if the provided link is reachable.
        :param link: The link to check reachability for.
        :param timeout: The timeout for the requests in seconds.
        :return: True if the link is reachable, False otherwise.
        """
        try:
            # Send a HEAD request to the link with allow_redirects set to True
            response = requests.head(link, allow_redirects=True, timeout=timeout)
            # Check if the status code of the response is between 200 and 299 slash
            if 200 <= response.status_code < 300:
                # Check redirection
                self.check_redirection(response, link)
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            # Log the error and re-raise it
            logger.warning("An error occurred while checking link reachability. Error: %s", e)
            raise e

    def check_redirection(self, response, link):
        """
        Check if the response is a redirection.
        :param response: The response object.
        :param link: The link that was checked.
        """
        if 'location' in response.headers:
            new_link = response.headers['location']
            logger.warning("The link %s redirects to %s", link, new_link)

    def check_methods(self, link: str) -> dict:
        """
        Check the available methods for a link.
        :param link: The link to check available methods for.
        :return: A dictionary containing the available methods and their statuses.
        """
        result = {}
        for method in self.methods:
            try:
                response = requests.request(method, link)
                result[method] = response.status_code
            except requests.exceptions.RequestException as e:
                result[method] = e
                logger.warning("An error occurred while checking %s method for %s. Error: %s", method, link, e)
        return result
