import sys
import requests
import json

url = sys.argv[1]

result = {"title":" User enumeration ","summary":"","recommendation":"","vulnerable":False}
vulnerable = False


def login_and_check_user(url, username, password):
    login_url = f"{url}/wp-login.php"

    # Prepare the payload with only the required fields
    payload = {
        'log': username,
        'pwd': password
    }

    # Headers can be important for the request
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
        'Referer': login_url,
        'Origin': url
    }

    # Send the login request and follow redirections
    response = requests.post(login_url, data=payload, headers=headers, allow_redirects=True)

    # Check the response for the username
    if username in response.text:
        result["summary"]="User Enumeration Found"
    else:
        result["summary"]="User not found or login failed"
       


# User inputs

username = "AbraCadabra"
password = "Sdhktoh35"

# Perform the login and check
login_and_check_user(url, username, password)
print(json.dumps(result))

