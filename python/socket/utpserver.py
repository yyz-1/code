import socket
import time

utpserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = '192.168.2.195'
port = 6633
laddr = (ip,port)

utpserver.bind(laddr)

while True:
    data,addr = utpserver.recvfrom(1024)

    print(data.decode('utf-8'),addr)

    msg = time.strftime("%Y/%m/%d %H:%M:%S")
    msg1 = "%s 【%s】" % (msg,data.decode('utf-8'))
    
    utpserver.sendto(msg1.encode('utf-8'),addr) #这里必须编码后才能发送