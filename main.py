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
    available_methods = []
    for method in methods:
        try:
            response = requests.request(method, link)
            if response.status_code != 405:
                available_methods.append(method)
        except:
            pass
    return available_methods


if __name__ == "__main__":
    main()
