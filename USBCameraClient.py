import os
from time import sleep
import sys
import numpy as np
import socket
import time

# init socket
ip_port = ('192.168.1.125', 30000)
buffer_size = 1024
cli = socket.socket()
print('Connect server ...')
cli.connect(ip_port) 

def main():
    i = 0
    while True:
        socket_send_back_data = str(i)
        cli.send(socket_send_back_data.encode('utf-8'))
        print('Client send signal %s' % socket_send_back_data)
        msg = cli.recv(buffer_size)
        str_rec = msg.decode('utf-8')
        print('Client receive back signal %s' % str_rec)
        i = i + 1
        sleep(3)

if __name__ == '__main__':
    main()