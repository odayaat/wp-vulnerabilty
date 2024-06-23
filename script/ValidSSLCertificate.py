import ssl
import sys
import socket
import datetime
import json

url = sys.argv[1]
result = {"title":"  Validate ssl ","summary":"","recommendation":"","vulnerable":False}
vulnerable = False

def scan_ssl_certificate(url):
    try:
        # Extract the hostname from the URL
        hostname = url.split('//')[1].split('/')[0]

        # Establish a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get SSL certificate
                cert = ssock.getpeercert()

                # Check certificate expiration date
                not_after_str = cert['notAfter']
                not_after_date = datetime.datetime.strptime(not_after_str, "%b %d %H:%M:%S %Y %Z")
                current_date = datetime.datetime.now()

                if not_after_date < current_date:
                    result["summary"]="SSL Certificate has expired!"
                else:
                    result["summary"]="SSL Certificate is valid."
                


        

    except Exception as e:
        result["summary"]+=f"Error: {e}"


# User input



# Scan SSL certificate
scan_ssl_certificate(url)
print(json.dumps(result))

