#!/usr/bin/python3

"""
Request to an URL using post Method
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        html_content = response.read().decode('utf-8')
        print(html_content)
