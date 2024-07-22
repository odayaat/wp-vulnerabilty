import json
import socket
import concurrent.futures
from urllib.parse import urlparse
import sys

result = {
    "title": "Port Scanning",
    "summary": "",
    "recommendation": "",
    "vulnerable": False,
}


def TCP_connect(ip, port_number, delay, output):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPsock:
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        TCPsock.settimeout(delay)
        try:
            TCPsock.connect((ip, port_number))
            output[port_number] = "Listening"
        except:
            output[port_number] = ""


def scan_ports(host_ip, delay):
    output = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {
            executor.submit(TCP_connect, host_ip, port, delay, output): port
            for port in range(10000)
        }
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            if output.get(port) == "Listening":

                result["summary"] = f"{port}: Listening\n"

                result["vulnerable"] = True
                result["recommendation"] = "Vulnerability detected!"


def main():
    input_url = sys.argv[1]
    parsed_url = urlparse(input_url)
    host_ip = parsed_url.hostname
    delay = 2
    scan_ports(host_ip, delay)

    if not result["vulnerable"]:
        result["summary"] = "No open ports detected"
        result["recommendation"] = "No vulnerability detected"

    print(json.dumps(result))


if __name__ == "__main__":
    main()
