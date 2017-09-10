#coding=utf-8
import socket
ip_port = ('127.0.0.1',9797)

sk = socket.socket()
sk.connect(ip_port)

try:
    while True:
        data = sk.recv(1024)
        print 'receive:',data
        inp = raw_input('please input:')
        sk.sendall(inp)
        if inp == 'exit':
            break

except Exception as e:
    print 'EEEEEEEEEEEEeee'
    sk.sendall('exit')
    sk.close()

# import socket
# import time
# import  traceback
# host = '127.0.0.1'
# port = 8083

# try:

#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
#     client.connect((host, port))
#     while True:
#         str = raw_input("Input: ");
#         client.send(str.encode())
#         # print('send data')
#         # time.sleep(1) #如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点

# except Exception as e:
#     print e
