import json
import re
import sys
import requests
from urllib.parse import urlparse

result = {
    "title": "URL Check",
    "summary": "",
    "recommendation": "",
    "vulnerable": False,
}


def validate_url(url):
    # Check if URL starts with http:// or https://
    if not url.startswith(("http://", "https://")):
        result["summary"] = "Invalid Url.\n"
        result["recommendation"] = " URL should start with http:// or https:// \n"
        result["vulnerable"] = True

    # Check if an IP address is provided
    ip_pattern = re.compile(r"^(http[s]?://)?(\d{1,3}\.){3}\d{1,3}(/|$)")
    if ip_pattern.match(url):
        result["summary"] += "Wrong url format\n"
        result["recommendation"] += "Make sure URL format matches standard format\n"
        result["vulnerable"] = True

    # Block the word 'localhost'
    if "localhost" in url:
        result["summary"] += "Localhost url not allowed\n"
        result["recommendation"] += "Make sure URL is not a local url\n"
        result["vulnerable"] = True

    # Block specific characters
    forbidden_characters = [">", "<", "'", '"', "=", ")", "(", "&", "%", "#"]
    if any(char in url for char in forbidden_characters):
        result["summary"] += "Suspicious characters found in url\n"
        result["recommendation"] += "The url characters are not valid"
        result["vulnerable"] = True

    # Check URL length
    if len(url) > 40:
        result["summary"] += "Invalid URL: URL length exceeds limit\n"
        result["recommendation"] += "Make sure URL length is within the limit\n"
        result["vulnerable"] = True

    parsed_url = urlparse(url)
    # Path Traversal Check
    if ".." in parsed_url.path:
        result["summary"] += "Invalid URL: Path traversal attack detected\n"
        result[
            "recommendation"
        ] += "Make sure URL does not contain path traversal characters\n"
        result["vulnerable"] = True

    # Check if the website is accessible
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            result["summary"] += "Invalid URL: Website is not accessible\n"
            result["recommendation"] += "Make sure the website is accessible\n"
            result["vulnerable"] = True
    except requests.exceptions.RequestException:
        result["summary"] += "Invalid URL: Website is not accessible\n"
        result["recommendation"] += "Make sure the website is accessible\n"
        result["vulnerable"] = True

    return result


site = sys.argv[1]

validate_url(site)

if not result["vulnerable"]:
    result["summary"] = "URL is valid"

print(json.dumps(result))
