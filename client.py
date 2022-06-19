#!/usr/bin/python3
from socket import socket, AF_INET, SOCK_STREAM


def main():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("", 8080))
    msg = input("Enter a message to send to the server: ")
    msg_bytes = msg.encode('utf-8')
    client.sendall(msg_bytes)
    print(f"Sending: {msg}")

    bytes_received = 0
    bytes_expected = len(msg)
    while bytes_received < bytes_expected:
        data = client.recv(1024)
        bytes_received += len(data)
        print(f"Received: {data.decode('utf-8')}")
    client.close()


if __name__ == "__main__":
    main()
