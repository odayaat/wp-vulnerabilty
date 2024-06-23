import requests
import json

url = "https://leharshim.com/"

result = {"title":" get themes  ","summary":"","recommendation":"","vulnerable":False}
vulnerable = False

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes

    # Search for lines containing 'wp-content/themes'
    theme_lines = [line for line in response.text.splitlines() if 'wp-content/themes' in line]

    # Extract URLs
    theme_urls = []
    for line in theme_lines:
        # Replace occurrences of href= or src= with a placeholder for easy parsing
        line = line.replace('href=', 'THIIIIS').replace('src=', 'THIIIIS')
        # Split the line using the placeholder and extract the URL
        parts = line.split('THIIIIS')
        for part in parts[1:]:
            url_parts = part.split("'")
            if len(url_parts) >= 2:
                theme_urls.append(url_parts[1])  # Extract URL enclosed in single quotes

    # Print extracted URLs
        result["summary"] = "Extracted themes URLs:\n" + "\n".join(theme_urls)


except requests.RequestException as e:
    result["summary"]+=f"GET request failed: {e}"
    
print(json.dumps(result))
