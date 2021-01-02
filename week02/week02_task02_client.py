import socket,sys,json,struct,time

HOST = 'localhost'
PORT = 10001

def test_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
    except Exception as err:
        print(err)
        sys.exit(1)
    while 1:
        head = s.recv(1024)
        if head:
            print('已连接服务端,等待接收数据')
        try:
            head_len = struct.unpack('i', head)[0]
        except Exception as err:
            print("head_len = struct.unpack('i', head)[0]报错执行continue")
            continue
        data = s.recv(head_len)  # 接收长度为head_len的报头内容的信息 (包含文件大小,文件名的内容)
        data = json.loads(data)
        FileName = data['FileName']
        FileSize = data['FileSize']
        recv_len = 0
        with open(FileName, 'wb') as w:
            while recv_len < FileSize:
                recv_mesg = s.recv(1024)
                if not recv_mesg:
                    print("s.close()")
                    s.close()
                print(recv_mesg)
                w.write(recv_mesg)
                recv_len += len(recv_mesg)
            break
    s.close()



if __name__ == "__main__":
    test_client()