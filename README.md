# **THIS REPO IS ARCHIVED**

---

# Link Checker

Link Checker is a command-line tool that checks the validity and reachability
of a list of links provided as input. It uses the argparse module to parse
command-line arguments, logging module for logging, logging_module to handle
exceptions, and result_handler to handle the results.

## Usage

To run the program, navigate to the directory containing the source code and
run the following command:

```Shell
python3 link_checker.py -l <logging_level> -o <output_filepath> <links>

```

Where:

- `logging_level` is the level of logging desired (e.g. DEBUG, INFO, WARNING, 
ERROR)
- `output_filepath` is the path to the file where the results will be saved
- `links` is a list of links to check

## Functionality

The program performs the following steps:

1. Parses the command-line arguments using the `argparse` module
2. Retrieves the links to check, logging level and output file path from the
parsed arguments
3. Configures the logger with the logging level provided
4. Exits if no links were provided
5. Initializes the results dictionary and the link checker
6. Checks each link 
   1. Validates the link
   2. Checks the reachability of the link 
   3. Retrieves the results for the link
7. Handles the results by saving them to the output file and displaying them on
   the console

## Requirements

The program requires the following modules to be installed:

- `argparse`
- `logging`

## Limitations

It currently only checks the reachability of the links, but it can be extended
to check other properties of the links.
It only handle the output to a file and display the output on the console, but
it can be extended to handle output to other destinations.

## Support

If you have any questions or issues with the program, please open an issue on
this repository.
