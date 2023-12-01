#!/usr/bin/python3

"""
Use Basic authentication to get
UserId at Github.
"""

import requests
import sys
import base64

if __name__ == "__main__":

    username = sys.argv[1]
    token = sys.argv[2]

    credentials = f"{username}:{token}"
    base64_credentials = base64.b64encode(credentials.encode
                                          ('utf-8')).decode('utf-8')
    headers = {'Authorization': f'Basic {base64_credentials}'}

    # Make the request to the GitHub API to get user information
    url = 'https://api.github.com/user'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # If the request is successful, display the user id
        user_id = response.json().get('id')
        print(user_id)
    else:
        # If there is an error, display the status code and response text
        print("None")
