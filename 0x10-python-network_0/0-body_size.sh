#!/bin/bash
# count the word content
curl -s "$1" | wc -c
