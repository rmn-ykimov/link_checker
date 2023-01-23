import re
import requests

def main():
    links = input("Enter a list of links: ").split()
    result = {}
    for link in links:
        if not check_link(link):
            print(f"The string {link} is not a link.")
            continue
        result[link] = check_methods(link)
    if not result:
        print("No valid links found.")
    else:
        print(result)


def check_link(link):
    pattern = re.compile(r'^https?://')
    match = pattern.match(link)
    if match:
        return True
    else:
        return False


def check_methods(link):
    methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS',
               'TRACE', 'PATCH']
    available_methods = list(filter(lambda method: method_status(link,method) != 405, methods))
    return available_methods

def method_status(link,method):
    try:
        response = requests.request(method, link)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking {method} method for {link}. Error: {e}")

if __name__ == "__main__":
    main()
