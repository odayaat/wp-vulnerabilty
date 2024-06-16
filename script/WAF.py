import requests

import sys

url = sys.argv[1]

payloads = [
    "' UNION SELECT 1",
    "<script>alert()</script>",
    "../../../../../windows.ini",
    "<img src=x onerror=alert(1)>",
    "<?php echo file_get_contents('/etc/passwd'); ?>",
    "%2e%2e%2f%2e%2e%2f%2e%2e%2f",
    "....//....//....//....//....//....//....//....//%00",
    "' OR 1=1 AND 1=CONVERT(INT, (SELECT CHAR(66)+CHAR(66)+CHAR(66))) --",
    "<SCRİPT/SRC=data:,alert(1)>",
]

blocked_payloads = []

for payload in payloads:
    params = {"foo": payload}
    response = requests.get(url, params=params,headers={"Accept-Charset":"utf-8"})
    if response.status_code == 403 or response.status_code == 404:
        blocked_payloads.append(payload)
    elif response.status_code == 200:
        pass
    else:
        print(
            f"Unexpected response code: {response.status_code} for payload '{payload.encode("utf-8")}'."
        )

if len(blocked_payloads) == len(payloads):
    print("WAF appears to be blocking all malicious payloads.")

if len(blocked_payloads) < len(payloads):
    print("WAF vulnerabilities")
    print("The following payloads were not blocked:")
    for payload in payloads[len(blocked_payloads) :]:
        print(payload.encode("utf-8")) 
        
