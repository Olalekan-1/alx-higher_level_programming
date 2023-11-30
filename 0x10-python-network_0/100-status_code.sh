#!/bin/bash
# get status code
curl -sLw "%{http_code}" -o /tmp/curl_output.txt "$1"
