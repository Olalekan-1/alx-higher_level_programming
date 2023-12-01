#!/usr/bin/python3

"""
print error code
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Make the request
    response = requests.get(url)

    # Display the body of the response
    print(response.text)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
