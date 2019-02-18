import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建 socket 对象

host = "192.168.2.160" # 本地ip
port = 9999 # 端口号

serversocket.bind((host, port)) # 绑定端口号

serversocket.listen(5) # 设置最大连接数，超过后排队

while True:
    clientsocket, addr = serversocket.accept()
    print("连接地址: %s" % str(addr)) # 打印客户端ip地址
    msg = 'hello  Socket ！' + "\r\n"
    clientsocket.send(msg.encode('utf-8')) # 向客户端发送应答消息
    clientsocket.close() # 关闭连接