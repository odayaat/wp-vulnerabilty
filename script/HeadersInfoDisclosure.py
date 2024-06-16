# This is a sample Python script.
#   another example for web with vuln headers: url = "https://www.hashomer.org.il/"

import sys

# Import requests library
import requests

# Define the URL to check
url = sys.argv[1]


# Define the headers that may disclose version or technology information
disclosure_headers = ["X-Powered-By", "Server"]

# Try to access the URL
try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code == 200:
        # The URL is accessible
        print("The URL is accessible")

        # Get the headers from the response
        headers = response.headers

        # Initialize a list to store the disclosure headers
        disclosure_headers_found = []

        # Loop through the disclosure headers
        for header in disclosure_headers:
            # Check if the header is present in the response
            if header in headers:
                # The header is present
                disclosure_headers_found.append(header)

        # Check if there are any disclosure headers
        if disclosure_headers_found:
            # Print the disclosure headers and their values
            print(
                "The following headers may disclose version or technology information:"
            )
            for header in disclosure_headers_found:
                print(header + ": " + headers[header])
        else:
            # No disclosure headers are present
            print(
                "No headers that may disclose version or technology information are present"
            )
    else:
        # The URL is not accessible
        print("The URL is not accessible")

except Exception as e:
    # An error occurred
    print("An error occurred:", e)
