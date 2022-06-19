#!/usr/bin/python3
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread

def handle_client(client: socket):
    while True:
        data = client.recv(1024)
        if len(data) == 0:
            client.close()
            break
        else:
            print(f"Received: {data.decode('utf-8')}")
            data_upper = data.decode('utf-8').upper()
            client.sendall(data_upper.encode('utf-8'))
            print(f"Sending: {data_upper}")


def main():
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(("", 8080))
    server.listen(5)
    while True:
        try:
            client_socket, client_address = server.accept()
            print(f"Accepted connection from {client_address}")
            client_thread = Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
        except KeyboardInterrupt:
            break
    server.close()
    print("Closed server socket")


if __name__ == "__main__":
    main()
