# https://medone.co.il/wp-content/uploads/
import sys
import requests

url = sys.argv[1]


directories = ["wp-content", "wp-includes", "/wp-content/uploads/"]
vulnerable = False

for directory in directories:
    directory_url = f"{url.rstrip('/')}/{directory}"
    try:
        response = requests.get(directory_url)
        if response.status_code == 200:
            print(
                f"The directory {directory} is accessible. Directory listening vulnerability!"
            )
            vulnerable = True
        elif response.status_code == 403:
            pass
        elif response.status_code == 404:
            pass
        else:
            print(
                f"Failed to retrieve directory {directory}. Status code:",
                response.status_code,
            )
    except requests.RequestException as e:
        print(f"An error occurred while accessing {directory}: {e}")

if not vulnerable:
    print("Not vulnerable to Directory listening.")
