import socket

utpclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ('192.168.2.195',6633)

utpclient.connect(ip_port)

while True:
    data = input('>>> ')
    if not data:
        break
    utpclient.sendto(data.encode('utf-8'),ip_port)
    data_db = utpclient.recvfrom(1024)

    #print(data_db)
#如果只有一个参数接收，所以信息都以元组的形式存储进去  (b'2020/08/16 10:01:35 \xe3\x80\x90dfdsa\xe3\x80\x91', ('192.168.2.195', 6633))

    print(data_db[0].decode('utf-8'))

utpclient.close()