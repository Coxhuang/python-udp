import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建 socket 对象

host = "192.168.2.160" # 本地ip地址
port = 9999 # 设置端口号

s.connect((host, port)) # 连接服务，指定主机和端口

msg = s.recv(1024) # 接收小于 1024 字节的数据

s.close()

print (msg.decode('utf-8'))