import json
import re
import requests


def validate_link(link):
    pattern = re.compile(r'^https?://')
    return pattern.match(link) is not None


def check_methods(link):
    methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS',
               'TRACE', 'PATCH']
    available_methods = []
    for method in methods:
        status = check_method_status(link, method)
        if status != 405:
            available_methods.append(method)
    return available_methods


def check_method_status(link, method):
    try:
        response = requests.request(method, link)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(
            f"An error occurred while checking {method} method for {link}. "
            f"Error: {e}")


def main():
    links = input("Enter a list of links: ").split()
    if not links:
        print("The list of links is empty.")
        return
    result = {}
    for link in links:
        if not validate_link(link):
            print(f"The string {link} is not a link.")
            continue
        result[link] = {}
        for method in check_methods(link):
            result[link][method] = check_method_status(link, method)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
