#!/usr/bin/python3

"""
print the value of X-request in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Make the request
    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
