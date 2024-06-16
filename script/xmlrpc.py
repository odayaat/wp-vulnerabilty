# Import requests library
import requests

import sys

base_url = sys.argv[1]

# Append the xmlrpc.php directory to the base URL
url = base_url + "/xmlrpc.php"


# Try to get the url
try:
    response = requests.get(url)
    # Check the status code
    if response.status_code != 404:
        # The url exists
        print("xmlrpc.php found")
        # Define the post request data
        data = """<?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>demo.sayHello</methodName> 
<params></params> 
</methodCall>"""
        # Send the post request
        post_response = requests.post(url, data=data)
        # Print the post response
        print(post_response.text)
    elif response.status_code == 404:
        # The url does not exist
        print("xmlrpc.php not found")
    else:
        # The url exists but returns a different status code
        print("xmlrpc.php found but returned status code", response.status_code)
except Exception as e:
    # Handle any exceptions
    print("An error occurred:", e)
