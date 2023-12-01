#!/usr/bin/python3

"""
fetch an URL using post method
and confirm if response is json format
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': q}

    # Make the POST request
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
