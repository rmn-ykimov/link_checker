import logging

import arg_parser
import logging_module
import result_handler
from link_checker import LinkChecker


def process_links(links, link_checker, result, logger):
    """
    Process a list of links by validating them, checking their reachability and
    checking the available methods on them.
    :param links: List of links
    :param link_checker: LinkChecker object
    :param result: Dictionary to store the results
    :param logger: Logger object
    """
    for link in links:
        logging_module.handle_exception(
            lambda: link_checker.validate_link(link), logger)
        logging_module.handle_exception(
            lambda: link_checker.check_link_reachability(link),
            logger)

        result[link] = {}
        for method in link_checker.check_methods(link):
            result[link][method] = link_checker.check_method_status(link,
                                                                    method)


def main():
    """
    Main function to run the program.
    """
    args = arg_parser.parse_args()

    links_to_check = args.links
    log_level = args.loglevel
    output_file = args.output

    logger = logging.getLogger()
    logger.setLevel(log_level)
    if not links_to_check:
        print("The list of links is empty.")
        return

    results = {}
    link_checker = LinkChecker()
    process_links(links_to_check, link_checker, results, logger)

    result_handler.handle_results(results, output_file="output.json",
                                  display_output=True)



if __name__ == "__main__":
    main()
