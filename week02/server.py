
import socket

HOST = 'localhost'
PORT = 10001

def socket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        print(f'Connected by {conn}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        conn.close()
    s.close()

def server_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(f"coon : {conn}")
        print(f"addr : {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        print(data)
        conn.close()
    s.close()

def server_socket01():
    s = socket.socket()
    s.bind((HOST,PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        if not data:
            continue
        s.sendall(data)
        conn.close()
    s.close()

if __name__ == "__main__":
    server_socket()

