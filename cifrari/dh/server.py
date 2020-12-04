"""
"""

import socket
from config import saddr, g, N
from sys import argv


def dh(b):
    return pow(g, b, N)


def key(A, b):
    return pow(A, b, N)


def hconn(conn, b, B):
    A = int(conn.recv(2048).decode())
    conn.send(str(B).encode())
    K = key(A, b)
    return K


def server():
    b = int(argv[1])
    B = dh(b)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conn.bind(saddr)
        conn.listen()
        while True:
            client, _ = conn.accept()
            K = hconn(client, b, B)
            print(K)


if __name__ == "__main__":
    server()
