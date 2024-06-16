import re
import requests
from urllib.parse import urlparse


def validate_url(url):
    # Check if URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        return "Invalid URL"

    # Check if an IP address is provided
    ip_pattern = re.compile(r'^(http[s]?://)?(\d{1,3}\.){3}\d{1,3}(/|$)')
    if ip_pattern.match(url):
        return "Invalid URL"

    # Block the word 'localhost'
    if 'localhost' in url:
        return "Invalid URL"

    # Block specific characters
    forbidden_characters = ['>', '<', "'", '"', '=', ')', '(', '&', '%', '#']
    if any(char in url for char in forbidden_characters):
        return f"Invalid URL: Attack detected"

    # Check URL length
    if len(url) > 40:
        return "Invalid URL"

    parsed_url = urlparse(url)
    # Path Traversal Check
    if '..' in parsed_url.path:
        return "Invalid URL: Attack detected"

    # Check if the website is accessible
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return "Invalid URL: Website is not accessible"
    except requests.exceptions.RequestException:
        return "Invalid URL: Website is not accessible"

    return "URL is valid"


# Rate limit implementation (example using a simple counter)
from time import time, sleep


class RateLimiter:
    def __init__(self, rate, per):
        self.rate = rate
        self.per = per
        self.allowance = rate
        self.last_check = time()

    def is_allowed(self):
        current = time()
        time_passed = current - self.last_check
        self.last_check = current
        self.allowance += time_passed * (self.rate / self.per)

        if self.allowance > self.rate:
            self.allowance = self.rate  # Cap the allowance

        if self.allowance < 1.0:
            return False  # Reject the request

        self.allowance -= 1.0
        return True  # Allow the request


rate_limiter = RateLimiter(5, 60)  # 5 requests per 60 seconds


def check_url_with_rate_limit(url):
    if not rate_limiter.is_allowed():
        return "Rate limit exceeded. Try again later."

    return validate_url(url)


# Example usage
url = input("Enter a URL to check: ")
result = check_url_with_rate_limit(url)
print(result.encode("uft-8"))
