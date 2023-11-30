#!/bin/bash
# use post method for json content type
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
