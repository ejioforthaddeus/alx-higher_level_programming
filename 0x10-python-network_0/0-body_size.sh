#!/bin/bash
# Script that takes in a URL, sends a request and displays the size of the body of the response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Error: No URL provided."
  echo "Usage: ./script.sh <URL>"
  exit 1
fi

# Send the request and store the response in a variable
response=$(curl -sI "$1")

# Extract the content-length from the response headers
content_length=$(echo "$response" | awk '/Content-Length/ {print $2}' | tr -d '\r')

# Check if the content-length is empty
if [ -z "$content_length" ]; then
  echo "Error: Unable to retrieve the size of the response body."
  exit 1
fi

# Display the size in bytes
echo "Size of the response body: $content_length bytes"
