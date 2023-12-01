#!/usr/bin/python3

"""
Handle Http Error
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')

            print("Body response:")
            print(html_content)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

