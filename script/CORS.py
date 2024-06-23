import sys

# need to check if the site accessible
import requests
import json


url = sys.argv[1]

evilurl = "https://evil.com"
# A list of Origin headers to test
origins = [evilurl, url]

result = {"title":"  Cors ","summary":"","recommendation":"","vulnerable":False}


# Loop through the origins and send requests
for origin in origins:
    # Set the Origin header
    headers = {"Origin": origin}
    # Send an OPTIONS request
    response = requests.options(url, headers=headers)
    # Get the ACAO header from the response
    acao = response.headers.get("Access-Control-Allow-Origin")
    # Print the result
    result["summary"]+=f"Origin: {origin}, ACAO: {acao}\n"
    # Check if the web server is vulnerable
    if acao:
        result["summary"] += f"Origin: {origin}, ACAO: {acao}\n"
        
        if acao == evilurl or (acao == "*" and origin == url):
            result["summary"] += "Vulnerable\n"
            result["vulnerable"] = True
        else:
            result["summary"] += "Not vulnerable\n"
    else:
        result["summary"] += f"Origin: {origin}, ACAO: None\n"
        result["summary"] += "Not vulnerable\n"

print(json.dumps(result))

