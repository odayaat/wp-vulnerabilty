#https://leharshim.com/ vulnerable
import requests
from bs4 import BeautifulSoup
import json

result = {"title":" Wp Version Check  ","summary":"","recommendation":"","vulnerable":False}
vulnerable = False

def get_wordpress_version(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_generator = soup.find('meta', attrs={'name': 'generator'})
            if meta_generator:
                generator_content = meta_generator.get('content', '')
                if 'WordPress' in generator_content:
                    version_index = generator_content.find('WordPress')
                    version = generator_content[version_index + 9:].split(',')[0].strip()
                    return version
        return "WordPress version not found"
    except Exception as e:
        return f"Error: {e}"

# Example usage:
url = input("Enter the WordPress site URL: ")
version = get_wordpress_version(url)
result["summary"]+=f"WordPress version: {version}"


version = version.replace(".", "")

# Define the URL and headers
url1 = "https://wpscan.com/api/v3/wordpresses"
url2 = f"{url1}/{version}"
headers = {
    "Authorization": "Token token=QJ2tytYl0U0qdRasBgA1q2XDexcdgEqeRwhyYEpDDks",
    "Accept": "application/json"
}

# Send the GET request
response = requests.get(url2, headers=headers)

# Print the response
#print(response.json())

res = response.json()
#print("Response:", res)
if 'insecure' in str(res):
    result["summary"]="insecure Wordpress Version"
  
else:
    pass

print(json.dumps(result))
