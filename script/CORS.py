import sys

# need to check if the site accessible
import requests

url = sys.argv[1]

evilurl = "https://evil.com"
# A list of Origin headers to test
origins = [evilurl, url]

# Loop through the origins and send requests
for origin in origins:
    # Set the Origin header
    headers = {"Origin": origin}
    # Send an OPTIONS request
    response = requests.options(url, headers=headers)
    # Get the ACAO header from the response
    acao = response.headers.get("Access-Control-Allow-Origin")
    # Print the result
    print(f"Origin: {origin}, ACAO: {acao}")
    # Check if the web server is vulnerable
    if acao == evilurl:
        print("Vulnerable")
    if acao == "*" and origin == url:
        print("Vulnerable")
    else:
        print("Not vulnerable")
