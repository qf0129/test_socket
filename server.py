#coding=utf-8
import SocketServer
import traceback 

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
            conn = self.request
            print '+++++++++++++++++'
            print self.client_address
            conn.sendall('我是多线程')
            Flag = True
            while Flag:
                try:
                    data = conn.recv(1024)
                    print data
                    if data == 'exit':
                        Flag = False
                    elif data == '0':
                        conn.sendall('您输入的是0')
                    else:
                        conn.sendall('请重新输入.')
                except Exception as e:
                    traceback.print_exc()
                    self.finsh()

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9797),MyServer)
    server.serve_forever()


    # server.shutdown()
    # server.server_close()

# import socket, thread

# class SocketServer():

#     BUF_SIZE = 1024
#     host = '0.0.0.0'
#     port = 8083

#     def new(self):
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server.bind((host, port))
#         server.listen(5)
#         thread.start_new_thread(self.listen_conn())

#     def listen_conn(self)
#         while True: 
#             client, address = server.accept() 
#             data = client.recv(BUF_SIZE)
#             print(data.decode())
#             # client.close() #连接不断开，长连接


    
