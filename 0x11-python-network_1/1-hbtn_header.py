#!/usr/bin/python3

"""
    print the value of the X-Request value
    in the response header
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        # Extract the value of the 'X-Request-Id' header
        request_id = response.headers.get('X-Request-Id')

        print(request_id)
