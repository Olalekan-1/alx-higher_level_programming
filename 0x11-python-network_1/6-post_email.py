#!/usr/bin/python3

"""
Make a request sing the post method
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = {'email': email}

    # Make the POST request
    response = requests.post(url, data=data)
    print(response.text)
