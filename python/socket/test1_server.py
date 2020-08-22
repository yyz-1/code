import socket
import sys

#创建 socket 对象，ip:prot tcp
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#写入IP地址或主机名
#lhost = socket.gethostname()
lhost = '127.0.0.1'
lport = 5566

#绑定端口
serversocket.bind((lhost,lport))

#设置最大链接数
serversocket.listen(5)

while True:
    #建立客户端连接
    clientsocket,addr = serversocket.accept()

    print("连接地址：%s" % str(addr))

    str_db = 'hello world! hi python!!!' + "\r\n"
    clientsocket.send(str_db.encode('utf-8'))
    clientsocket.close()
