# This script runs on Python 3
import socket, threading
import sys


def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = "Listening"
    except:
        output[port_number] = ""


def scan_ports(host_ip, delay):
    isportopen = False


    threads = []  # To run TCP_connect concurrently
    output = {}  # For printing purposes

    # Spawning threads to scan ports
    for i in range(10000):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(10000):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(10000):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(10000):
        if output[i] == "Listening":
            print(str(i) + ": " + output[i])
            isportopen = True

    if not isportopen :
        print("no open port")


def main():
    host_ip = sys.argv[1]
    delay = 2
    scan_ports(host_ip, delay)


if __name__ == "__main__":
    main()
