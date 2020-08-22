import socket
import time

utp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = '192.168.2.195'   #请不要在忘记这个 括号 了
port = 45654

utp_server.bind((ip,port))

clidb = {}  #{addr:data}

print("server is open ")
while True:
    try:
        data,addr = utp_server.recvfrom(1024)
        print(data.decode('utf-8'),addr)

        if addr not in clidb:
            for address in clidb:
                fanh = "------welcome %s-------" % data.decode('utf-8')
                utp_server.sendto(fanh.encode('utf-8'),address)
            clidb[addr] = data.decode('utf-8')
            continue
        
        if "quit()" in data.decode('utf-8'):
            username = clidb[addr]
            clidb.pop(addr)
            for address in clidb:
                fanh = r"\\\\%s quit////" % username
                utp_server.sendto(fanh.encode('utf-8'),address)
        else:
            name = clidb[addr]
            msg = time.strftime("%Y/%m/%d %H:%M:%S")
            msg1 = "%s %s 【%s】" % (name,msg,data.decode('utf-8'))
            for address in clidb:
                if address != addr:
                    utp_server.sendto(msg1.encode('utf-8'),address)
    except ConnectionResetError:
        print("[Error] 远程主机强迫关闭了一个现有的连接")