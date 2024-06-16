import sys

# Import requests library
import requests

# Define the URL to check
url = sys.argv[1]


# Define the security headers to look for
security_headers = [
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "X-XSS-Protection",
    "Content-Security-Policy",
    "Referrer-Policy",
]

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

        # Initialize a list to store the missing headers
        missing_headers = []

        # Loop through the security headers
        for header in security_headers:
            # Check if the header is present in the response
            if header not in headers:
                # The header is missing
                missing_headers.append(header)

        # Check if there are any missing headers
        if missing_headers:
            # Print the missing headers
            print(
                "The following security headers are missing:",
                ", ".join(missing_headers),
            )
        else:
            # All security headers are present
            print("All security headers are present")
    else:
        # The URL is not accessible
        print("The URL is not accessible")

except Exception as e:
    # An error occurred
    print("An error occurred:", e)
