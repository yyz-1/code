import socket
import sys

#创建 socket 对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#这里的 IP 地址 填的是 服务端 的 IP 地址 
#host = socket.gethostname()    同是在本机测试时，客户端可以用 gethostname
rhost = '127.0.0.1'

#要访问的端口
rport = 5566 #这里设置都端口 必须 与 服务端设置的端口一致，否则报错

'''
address = (host,port)
print(address)  #('WIN-10', 5566)
'''

#连接服务，指定主机和端口
s.connect((rhost,rport))

#接收小于 1024 字节的数据
db_data = s.recv(1024)  #接收 tcp 数据

s.close()   #关闭连接

print(db_data.decode('utf-8'))