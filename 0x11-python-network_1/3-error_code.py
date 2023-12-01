#!/usr/bin/python3

"""
Handle Http Error
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')

            print(html_content)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
