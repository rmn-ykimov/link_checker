import logging
import requests

from urllib.parse import urlparse

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
        Validate if the link is valid or not, it is intended to use only for
        http and https protocols :param link: link to be validated :return:
        True if valid otherwise raises an exception
        """
        parsed_url = urlparse(link)
        # check if the link is valid or not
        if not parsed_url.scheme or not parsed_url.netloc:
            raise Exception(f"The string {link} is not a valid link.")
        if parsed_url.scheme not in ['http', 'https']:
            raise Exception(f"The link {link} is not a valid http or https "
                            f"protocol link.")
        return True

    def check_methods(self, link: str) -> list:
        """
        Check available methods on a link.
        :param link: Link to check methods on
        :return: List of available methods
        """
        available_methods = []
        for method in self.methods:
            try:
                status = self.check_method_status(link, method)
                if status != 405:
                    available_methods.append(method)
            except Exception as e:
                logger.error(f"An error occurred: {e}")
        return available_methods

    def check_method_status(self, link: str, method: str) -> int:
        """
        Check the status of a method on a link.
        :param link: Link to check method on
        :param method: Method to check
        :return: HTTP status code of the method
        """
        try:
            response = requests.request(method, link)
            if response.status_code != 200:
                raise Exception(
                    f"Link returned status code {response.status_code}")
            return response.status_code
        except requests.exceptions.RequestException as e:
            raise Exception(
                f"An error occurred while checking {method} method for {link}."
                f" Error: {e}")

    def check_link_reachability(self, link: str) -> None:
        try:
            response = requests.head(link, allow_redirects=True)
            if response.status_code != 200:
                raise Exception(f"The link {link} is not reachable.")
        except requests.exceptions.RequestException as e:
            raise Exception(
                f"An error occurred while checking reachability of {link}. "
                f"Error: {e}")
