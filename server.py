#coding=utf-8
from SocketServer import ThreadingTCPServer, BaseRequestHandler, ThreadingMixIn, TCPServer
import traceback 
from shortuuid import uuid
from datetime import datetime
from config import SERVER_HOST, SERVER_PORT

class MyTcpServer(ThreadingMixIn, TCPServer):
    def __init__(self, server_address, RequestHandlerClass,):
        TCPServer.__init__(self, server_address, RequestHandlerClass,)
        self.conns = []

    def get_all_conns(self):
        return self.conns


class MainServer():
    def __init__(self):
        self.server = None

    def run(self):
        self.server = MyTcpServer((SERVER_HOST,SERVER_PORT),MyRequestHandler)
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()

# class RoomManage():
#     rooms = []

#     def new():


#         rooms.append({
#             'id': uuid(),
#             'created_time': datetime.now(),
#             'server': server
#             })


#     def get_all_rooms():
#         return rooms


class MyRequestHandler(BaseRequestHandler):

    def handle(self):
        self.handle_conn(self.request)

    def handle_conn(self, conn):
        self.save_conn(conn)

        Flag = True
        while Flag:
            try:
                self.handle_msg(conn)
            except Exception as e:
                traceback.print_exc()
                self.break_conn(conn)
                Flag = False



    def save_conn(self, conn):
        self.server.conns.append({
            'id': uuid(),
            'created_time': datetime.now(),
            'address': self.client_address,
            'conn': conn})

        print(str(self.client_address) + ' conn success! All:'+str(self.server.get_all_conns()))
        conn.sendall('conn success! Your address is ' + str(self.client_address))

    def handle_msg(self, conn):
        data = conn.recv(1024)
        print data
        if data == 'exit':
            Flag = False
        elif data == '0':
            conn.sendall('您输入的是0')
        else:
            conn.sendall('请重新输入.')

        self.send_to_all(data)

    def break_conn(self, conn):
        print(str(self.client_address) + ' conn break!')
        conn.close()

    def send_to_all(self, data):
        conns = self.server.get_all_conns()
        for conn in conns:
            conn['conn'].sendall(data)