import socket

# socket.AF_INET : 标识为IPv4地址
# socket.SOCK_STREAM ：标识为TCP协议（还有一种协议为UDP）
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

s.connect(('www.httpbin.org', 80))

print(s)

s.send()#baocuo

buffer = []

while True:
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break
s.close()

response = b''.join(buffer)

print(response)