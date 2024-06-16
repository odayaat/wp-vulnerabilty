import sys
import requests

url = sys.argv[1]

directories = [
    "/wp-backup.php.old",
    "/backup.php.old",
    "/config.php.old",
    "/wp-config.php.old",
    "/wp-config.php",
    "/config.php",
    "/backup.php",
    "/info.php",
]
vulnerable = False

for directory in directories:
    directory_url = f"{url.rstrip('/')}{directory}"
    try:
        response = requests.get(directory_url)
        if response.status_code == 200:
            print(f"The file or directory {directory} is accessible.")
            vulnerable = True
        elif response.status_code == 403:
            pass
        elif response.status_code == 404:
            pass
        else:
            pass
    except requests.RequestException as e:
        pass

if not vulnerable:
    print("No sensitive files or directories found.")
