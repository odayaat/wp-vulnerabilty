#https://medone.co.il/wp-content/uploads/
import requests
import sys
import json

url = sys.argv[1]

directories = ['wp-content', 'wp-includes', '/wp-content/uploads/']
vulnerable = False

result = {"title":" Direcgtory Listening ","summary":"","recommendation":"","vulnerable":False}


for directory in directories:
    directory_url = f"{url.rstrip('/')}/{directory}"
    try:
        response = requests.get(directory_url)
        if response.status_code == 200:
            result["summary"]+=f"The directory {directory} is accessible. Directory listening vulnerability!"
            vulnerable = True
        elif response.status_code == 403:
            pass
        elif response.status_code == 404:
            pass
        else:
            result["summary"]-=f"Failed to retrieve directory {directory}. Status code:", response.status_code
    except requests.RequestException as e:
        result["summary"]+=f"An error occurred while accessing {directory}: {e}"
       

if not vulnerable:
    result["summary"]="Not vulnerable to Directory listening."
    
print(json.dumps(result))
    