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
            lambda: link_checker.validate_link(link), logger)

        # Check the reachability of the link
        logging_module.handle_exception(
            lambda: link_checker.check_link_reachability(link),
            logger)

        # Retrieve the results for the link
        results[link] = {}
        for method in link_checker.check_methods(link):
            results[link][method] = link_checker.check_method_status(link,
                                                                     method)

    # Handle the results
    result_handler.handle_results(results, output_file=output_filepath,
                                  display_output=True)


if __name__ == "__main__":
    main()
