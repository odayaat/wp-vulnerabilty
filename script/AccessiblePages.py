#https://allorav.com
import sys
import requests
import json

url = sys.argv[1]

directories = ['/wp-backup.php.old', '/backup.php.old', '/config.php.old',
               '/wp-config.php.old', '/wp-config.php', '/config.php',
               '/backup.php', '/info.php']
vulnerable = False
result = {"title":" Assecible pages ","summary":"","recommendation":"","vulnerable":False}

for directory in directories:
    directory_url = f"{url.rstrip('/')}/{directory}"
    try:
        response = requests.get(directory_url)
        if response.status_code == 200:
            result["summary"]+=f"The file or directory {directory} is accessible.\n"
            vulnerable = True
        elif response.status_code in {403, 404}:
            pass
        else:
            pass
    except requests.RequestException as e:
        pass
if(vulnerable):
    result["recommendation"]="""These accessible files and directories can contain sensitive information such as configuration details, database credentials, and backup data, which may be exploited by attackers to gain unauthorized access to the system or its data.
Recommendations:
1. Remove Unnecessary Files:
   - Delete any old or unused files.
2. Restrict Access:
   - Configure the web server to prevent access to sensitive files.
3. Set Proper Permissions:
   - Ensure sensitive files have restrictive permissions.
4. Disable Directory Listing:
   - Prevent directory contents from being listed.
5. Implement Access Controls:
   - Use authentication and IP whitelisting to restrict access.
6. Secure Backups:
   - Store backups securely and ensure they are not web-accessible.
7. Environment Segregation:
   - Keep development and production environments separate.
8. Use a Web Application Firewall (WAF):
   - Deploy a WAF to block attempts to access sensitive files.
"""
    result["vulnerable"]=True


else:
    result["summary"]="No accessible sensitive files or directories were found."


print(json.dumps(result))

