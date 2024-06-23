# This is a sample Python script.
#   another example for web with vuln headers: url = "https://www.hashomer.org.il/"

import sys

# Import requests library
import requests
import json


# Define the URL to check
url = sys.argv[1]

result = {"title":" Headers info disclosure User ","summary":"","recommendation":"","vulnerable":False}
vulnerable = False


# Define the headers that may disclose version or technology information
disclosure_headers = ["X-Powered-By", "Server"]

# Try to access the URL
try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code == 200:
        # The URL is accessible
        result["summary"]="The URL is accessible"

        # Get the headers from the response
        headers = response.headers

        # Initialize a list to store the disclosure headers
        disclosure_headers_found = []

        # Loop through the disclosure headers
        for header in disclosure_headers:
            # Check if the header is present in the response
            if header in headers:
                # The header is present
                disclosure_headers_found.append(f"{header}: {headers[header]}")

        # Check if there are any disclosure headers
        if disclosure_headers_found:
            # Print the disclosure headers and their values
            result["summary"] += "The following headers may disclose version or technology information:\n"
            result["summary"] += "\n".join(disclosure_headers_found)
            result["vulnerable"] = True

            
            for header in disclosure_headers_found:
                result["summary"]+=header + ": " + headers[header]
            
        else:
            # No disclosure headers are present
            result["summary"]="No headers that may disclose version or technology information are present"

    else:
        # The URL is not accessible
        result["summary"]="The URL is not accessible"
        result["vulnerable"] = True


except Exception as e:
    # An error occurred
    result["summary"] = f"An error occurred: {e}"
print(json.dumps(result))
