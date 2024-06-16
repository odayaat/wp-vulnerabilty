# get the site URL from the user
import sys

sys.path.insert(0, "env/lib/python3.11/site-packages")


import requests as requests

site = sys.argv[1]

# append /wp-admin to the site URL
wp_admin = site + "/wp-admin"

# send a GET request to the /wp-admin URL and allow redirections
response = requests.get(wp_admin, allow_redirects=True)

# get the status code and the content of the response
status = response.status_code
content = response.text

# print("""\{ "title":"Le titre", "message":"Le message" \}""")

# check if the status code is 200 (OK)
if status == 200:
    # check if the content contains "wp-login" or "wp-admin"
    if "wp-login" in content or "wp-admin" in content:
        # print that /wp-admin is accessible
        print(f"/wp-admin is accessible on {site}")
    else:
        # print that /wp-admin is not accessible
        print(f"/wp-admin is not accessible on {site}")
else:
    # print that /wp-admin is not accessible
    print(f"/wp-admin is not accessible on {site}")
