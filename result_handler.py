import json


def handle_results(results, output_file=None, display_output=False):
    if display_output:
        print(json.dumps(results, indent=4))
    elif output_file:
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=4)
    else:
        print("No output file or display option specified.")
