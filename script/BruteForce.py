# https://chriscoyier.net/?s=revjiu
import sys
import requests
import threading
import json


# User inputs
url = sys.argv[1]

# Perform the search requests
vulnerable = False
result = {"title":" Brute Force ","summary":"","recommendation":"","vulnerable":False}



def send_search_request(search_url, success_counter):
    try:
        response = requests.get(search_url)

        if response.status_code == 200:
            success_counter.append(1)
    except requests.RequestException as e:
        result["summary"]=""


def send_search_requests(url):
    search_url = f"{url}/?s=vdsvsd"
    threads = []
    success_counter = []

    for i in range(34):
        thread = threading.Thread(target=send_search_request, args=(search_url, success_counter))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if len(success_counter) == 34:
        result["summary"]= "Vulnerable to Brute Force Attacks"


send_search_requests(url)
print(json.dumps(result))

