import socket

HOST = 'localhost'
PORT = 10000

def echo_seocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        data = input("input >>>")
        if data == 'exit':  # 判断客户端输入的是不是exit，是的话直接退出，截断链接
            break
        s.sendall(data.encode('utf-8'))# 向服务端发送客户端输入的全部信息
        data = s.recv(1024)  # 等待接收服务端回复的信息
        if not data:
            break
        else:
            print(data.decode('utf-8'))
    s.close()

def client_socket():
    s = socket.socket()
    s.connect((HOST, PORT))
    while True:
        data = input("input >>>")
        if data == 'exit':
            break
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))
    s.close()

def client_socket01():
    s = socket.socket()
    s.connect((HOST,PORT))
    while True:
        data = input('input >>>')
        if data == 'exit':
            break
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))
    s.close()



if __name__ == "__main__":
    client_socket()


