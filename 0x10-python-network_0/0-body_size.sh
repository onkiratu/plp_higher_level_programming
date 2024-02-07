#!/bin/bash
# Script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
URL="$1"
curl -is $URL | grep "Content-Length" | tail -n 1 | awk '{print $2}'
