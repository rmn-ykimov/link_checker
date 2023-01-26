"""
This script is a link checker. It reads a list of links from command line arguments
and checks their validity and reachability.
The script uses argparse to parse command-line arguments, logging to handle logging,
logging_module to handle exceptions, and result_handler to handle the final results.
The LinkChecker class from the link_checker module is used to perform the link checks.
The results are output to a specified file or to the terminal.
"""
import logging
import arg_parser
import logging_module
import result_handler
from link_checker import LinkChecker

def main():
    """
    Main function to run the program.
    """
    # Parse the command line arguments
    parsed_arguments = arg_parser.parse_args()

    # Retrieve the links to check, logging level and output file path
    links = parsed_arguments.links
    logging_level = parsed_arguments.loglevel
    output_filepath = parsed_arguments.output

    # Configure the logger
    logger = logging.getLogger()
    logger.setLevel(logging_level)

    # Exit if no links were provided
    if not links:
        print(
            "No links were provided for checking. Please provide a list of "
            "links and try again.")
        return

    # Initialize the results dictionary and the link checker
    results = {}
    link_checker = LinkChecker()

    # Check each link
    for link in links:
        # Validate the link
        logging_module.handle_exception(
            lambda link=link: link_checker.validate_link(link), logger)

        # Check the reachability of the link
        logging_module.handle_exception(
            lambda link=link: link_checker.check_link_reachability(link),
            logger)

        # Retrieve the results for the link
        results[link] = link_checker.check_methods(link)




    # Handle the results
    result_handler.handle_results(results, output_file=output_filepath,
                                  display_output=True)


if __name__ == "__main__":
    main()
