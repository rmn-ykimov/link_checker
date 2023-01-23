import json
import re
import requests

# This function validates if the given link is valid, it is intended to use only for http and https protocols
def validate_link(link):
    # Regular expression pattern for http and https
    pattern = re.compile(r'^https?://')
    # check if the link is valid or not
    if not pattern.match(link):
        # If the link is not valid, raise an exception
        raise Exception(f"The string {link} is not a valid link.")
    return True

# This function checks available methods on the given link
def check_methods(link):
    # List of all possible http methods
    methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
    # Initialize an empty list to store available methods
    available_methods = []
    for method in methods:
        try:
            status = check_method_status(link, method)
            # if the status code is not 405, method is considered as available
            if status != 405:
                available_methods.append(method)
        except Exception as e:
            print(f"An error occurred: {e}")
    return available_methods

# This function checks the status of the given method on the given link
def check_method_status(link, method):
    try:
        # send request to the link for the given method
        response = requests.request(method, link)
        # check if the response status code is not 200
        if response.status_code != 200:
            # Raise an exception if the status code is not 200
            raise Exception(f"Link returned status code {response.status_code}")
        return response.status_code
    except requests.exceptions.RequestException as e:
        # Raise an exception if an error occurs while making the request
        raise Exception(f"An error occurred while checking {method} method for {link}. Error: {e}")

def main():
    links = input("Enter a list of links: ").split()
    if not links:
        print("The list of links is empty.")
        return
    result = {}
    for link in links:
        try:
            validate_link(link)
            result[link] = {}
            for method in check_methods(link):
                result[link][method] = check_method_status(link, method)
        except Exception as e:
            print(f"An error occurred: {e}")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
