#coding=utf-8
from config import SERVER_HOST, SERVER_PORT
import socket
import traceback 
import thread

def recv(conn):
    flag = True
    while flag:
        try:
            data = conn.recv(1024)
            print 'receive:',data
        except Exception as e:
            traceback.print_exc()
            flag = False


conn = socket.socket()
conn.connect((SERVER_HOST,SERVER_PORT))

thread.start_new_thread(recv, (conn,))

try:
    while True:
        inp = raw_input('please input:')
        conn.sendall(inp)
        # if inp == 'exit':
        #     break

except Exception as e:
    conn.sendall('exit')
    conn.close()
    traceback.print_exc()
    exit()