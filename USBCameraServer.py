import os
from time import sleep
import sys
import numpy as np
import socket
import time

# init socket
ip_port = ('192.168.1.125', 30000)
back_log = 5
buffer_size = 1024
ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ser.bind(ip_port)
ser.listen(back_log)

def main():
    i = 10
    print('Waiting for client to connect ...')
    con, address = ser.accept()
    while True:
        print('Waiting for client to send data ...')
        msg = con.recv(buffer_size)
        str_rec = msg.decode('utf-8')
        print('Server receive signal %s' % str_rec)
        socket_send_back_data = str(i)
        con.send(socket_send_back_data.encode('utf-8'))
        print('Server send back signal %s' % socket_send_back_data)
        i = i + 1
        sleep(1)

if __name__ == '__main__':
    main()