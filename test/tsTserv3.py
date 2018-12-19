#!/usr/bin/env python

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (bytes(ctime(), 'utf-8'), data)).encode())
        print(addr,': ',data.decode())
        print(('re: [%s] %s' % (bytes(ctime(), 'utf-8'), data)).encode())
    tcpCliSock.close()
tcpSerSock.close()
