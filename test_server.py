#_*_coding:utf-8_*_

import socket
import select

s = socket.socket()
s.bind(('localhost', 10000))
s.listen(5)
epoll_obj = select.epoll()
epoll_obj.register(s,select.EPOLLIN)
connections = {}
while True:
 events = epoll_obj.poll()
 for fd, event in events:
  print(fd,event)
  if fd == s.fileno():
   conn, addr = s.accept()
   connections[conn.fileno()] = conn
   epoll_obj.register(conn,select.EPOLLIN)
   msg = conn.recv(200)
   conn.sendall('ok'.encode())
  else:
   try:
    fd_obj = connections[fd]
    msg = fd_obj.recv(200)
    fd_obj.sendall('ok'.encode())
   except BrokenPipeError:
    epoll_obj.unregister(fd)
    connections[fd].close()
    del connections[fd]

s.close()
epoll_obj.close()


# import socket,select  
  
# s=socket.socket()  
# host='localhost' 
# port=10000  
# s.bind((host,port))  
  
# s.listen(5)  
  
# inputs=[s]  
# while True:  
#     rs,ws,es=select.select(inputs,[],[])  #1、select函数阻塞进程，直到inputs中的套接字被触发（在此例中，套接字接收到客户端发来的握手信号，从而变得可读，满足select函数的“可读”条件），rs返回被触发的套接字（服务器套接字）；  
#                                             # 4、select再次阻塞进程，同时监听服务器套接字和获得的客户端套接字；  
  
#     for r in rs:  
#         if r is s:                          #2、如果是服务器套接字被触发（监听到有客户端连接服务器）  
#             c, addr = s.accept()  
#             print('Got connection from', addr)  
#             inputs.append(c)                #3、inputs加入客户端套接字  
#         else:                               #5、当客户端发送数据时，客户端套接字被触发，rs返回客户端套接字，然后进行下一步处理。  
#             try:  
#                 data=r.recv(1024)  
#                 disconnected=not data  
#             except socket.error:  
#                 disconnected = True  

#             if disconnected:  
#                 print(r.getpeername(),'disconnected')  
#                 inputs.remove(r)  
#             else:  
#                 print(data,str(inputs))