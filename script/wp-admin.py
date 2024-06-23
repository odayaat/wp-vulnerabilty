# get the site URL from the user
import requests as requests
import sys
import json
url = sys.argv[1]


# append /wp-admin to the site URL
wp_admin = url + "/wp-admin"

result = {"title":"  Word Press admin ","summary":"","recommendation":"","vulnerable":False}
vulnerable = False

# send a GET request to the /wp-admin URL and allow redirections
response = requests.get(wp_admin, allow_redirects=True)

# get the status code and the content of the response
status = response.status_code
content = response.text

# check if the status code is 200 (OK)
if status == 200:
    # check if the content contains "wp-login" or "wp-admin"
    if "wp-login" in content or "wp-admin" in content:
        # print that /wp-admin is accessible
        result["summary"]+=f"/wp-admin is accessible on {url}"
        vulnerable= True
        if(vulnerable):
            result["recommendation"]=""""The WordPress wp-admin page is the administrative interface where site administrators can manage content, themes, plugins, and other critical settings. Unauthorized access to this page can lead to severe security risks, including site defacement, data breaches, and complete takeover of the website.
Recommendations:
1. Use Strong Authentication:
Ensure strong, unique passwords are used for all administrative accounts.
Implement multi-factor authentication (MFA) to add an extra layer of security.

2. Limit Access by IP:
Restrict access to the wp-admin page by allowing only trusted IP addresses.

3.Implement Security Plugins:
Use security plugins like Wordfence or Sucuri to enhance the protection of your WordPress site and monitor for unauthorized access attempts.

4. Rename Login URL:
Use plugins or custom configurations to change the default login URL from /wp-admin to something less predictable.
"""
     
    else:
        # print that /wp-admin is not accessible
        result["summary"]+=f"/wp-admin is not accessible on {url}"
else:
    # print that /wp-admin is not accessible
    result["summary"]+=f"/wp-admin is not accessible on {url}"
print(json.dumps(result))

    
