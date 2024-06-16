import sys
import requests

url = sys.argv[1]


try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes

    # Search for lines containing 'wp-content/themes'
    theme_lines = [
        line for line in response.text.splitlines() if "wp-content/themes" in line
    ]

    # Extract URLs
    theme_urls = []
    for line in theme_lines:
        # Replace occurrences of href= or src= with a placeholder for easy parsing
        line = line.replace("href=", "THIIIIS").replace("src=", "THIIIIS")
        # Split the line using the placeholder and extract the URL
        parts = line.split("THIIIIS")
        for part in parts[1:]:
            url_parts = part.split("'")
            if len(url_parts) >= 2:
                theme_urls.append(url_parts[1])  # Extract URL enclosed in single quotes

    # Print extracted URLs
    for url in theme_urls:
        print(url)

except requests.RequestException as e:
    print(f"GET request failed: {e}")
