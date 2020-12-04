"""
"""

import socket
from config import saddr, g, N
from sys import argv


def dh(a):
    return pow(g, a, N)


def key(B, a):
    return pow(B, a, N)


def client():
    a = int(argv[1])
    A = dh(a)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conn.connect(saddr)

        conn.send(str(A).encode())
        B = int(conn.recv(2048).decode())
        K = key(B, a)

        print(K)


if __name__ == "__main__":
    client()
