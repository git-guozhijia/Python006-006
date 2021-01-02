import socket
from pathlib import Path
import os
import json
import struct
import time

HOST = 'localhost'
PORT = 10001

def getFileInfo(filePath):
	file = filePath.strip()
	if not Path.is_file(Path(file)):
		print("上传的文件路径错误")

	FileSize = os.path.getsize(file)
	FileName = 'new_' + str(Path(file).name)
	dirc = {
		'FileName': FileName,
		'FileSize': FileSize,
	}
	head_info = json.dumps(dirc)
	head_info_len = struct.pack('i', len(head_info))
	# head_info_len = len(head_info)
	return head_info_len,head_info,file

def test_server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		print(f"链接人信息 : {conn}")
		while True:
			time.sleep(5)
			if not conn:
				print("链接客户端失败")
				break
			FilePath = input("输入文件路径>>>")
			# 获取文件信息
			head_info_len,head_info,file_path = getFileInfo(FilePath)
			# 发送文件信息的信息长度，给客户端
			conn.sendall(head_info_len)
			# 发送文件信息给客户端
			conn.sendall(head_info.encode('utf-8'))
			try:
				with open(file_path, 'rb') as f:
					while 1:
						data = f.read(1024)
						if not data:
							print("读取的内容已经完成")
							break
						print(f"data.decode('utf-8') >>> {data}\n")
						conn.sendall(data)
					break
			except Exception as err:
				print(f"读取文件报错：{err}")
				break
		conn.close()
	s.close()

if __name__ == "__main__":
	# test_server()
	# print(getFileInfo(' /Users/qtt/Desktop/git-guozhijia/week02/pathlib_t.py '))
	test_server()

