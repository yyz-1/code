import socket
import threading

def recv(utp_client,addr):
    utp_client.sendto(youname.encode('utf-8'),addr)
    while True:
        data = utp_client.recvfrom(1024)
        print(data[0].decode('utf-8'))    
    
    return


def send(utp_client,addr):
    while True:
        data = input()
        utp_client.sendto(data.encode('utf-8'),addr)
        if data == "quit()":
            break     

    return


def main():
    utp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    ip_port = ('192.168.2.195',45654)

    utp_client.connect(ip_port)

    threadingreve = threading.Thread(target=recv,args=(utp_client,ip_port),daemon=True)
    threadingsend = threading.Thread(target=send,args=(utp_client,ip_port))


    threadingreve.start()
    threadingsend.start()

    threadingsend.join()    #会报错OSError

    utp_client.close()

if __name__ == "__main__":
    youname = input("your name?")
    main()
