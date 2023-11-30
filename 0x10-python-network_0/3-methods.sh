#!/bin/bash
# the allowed method by Server
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
