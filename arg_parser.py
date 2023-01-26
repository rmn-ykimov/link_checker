"""
arg_parser.py - This module contains the parse_args() function which parses
command line arguments for a script that checks the methods and status codes of
a list of links. The parse_args() function takes in the following arguments:

links: a list of links to check (example : https://www.example.com)
-l or --loglevel: set the logging level (choices: 'DEBUG', 'INFO', 'WARNING',
'ERROR', 'CRITICAL') default: WARNING
-t or --timeout: set the timeout for the requests in seconds (default : 30)
-o or --output: write the output to a file (example : /path/to/file.txt)
"""
import argparse

def parse_args():
    """
    Parse command line arguments and returns the result
    :return: an argparse.Namespace object containing the parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Check the methods and status codes of a list of links.")
    parser.add_argument('links', metavar='link', type=str, nargs='+',
                        help='List of links to check. Example : https://www.example.com')
    parser.add_argument('-l', '--loglevel', type=str, default='WARNING',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR',
                                 'CRITICAL'],
                        help='Set the logging level. Default : WARNING')
    parser.add_argument('-t', '--timeout', type=int, default=30,
                        help='Set the timeout for the requests in seconds. Default : 30')
    parser.add_argument('-o', '--output', type=str,
                        help='Write the output to a file. Example : /path/to/file.txt')

    return parser.parse_args()
    