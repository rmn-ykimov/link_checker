import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check the methods and status codes of a list of links.")
    parser.add_argument('links', metavar='link', type=str, nargs='+',
                        help='List of links to check')
    parser.add_argument('-l', '--loglevel', type=str, default='WARNING',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR',
                                 'CRITICAL'],
                        help='Set the logging level')
    parser.add_argument('-t', '--timeout', type=int, default=30,
                        help='Set the timeout for the requests in seconds')
    parser.add_argument('-o', '--output', type=str,
                        help='Write the output to a file')

    return parser.parse_args()
