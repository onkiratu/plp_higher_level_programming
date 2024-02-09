#!/bin/bash
# a Bash script that takes in a URL, sends a POST request to the passed URL
curl -d "email: test@gmail.com" "$1"
