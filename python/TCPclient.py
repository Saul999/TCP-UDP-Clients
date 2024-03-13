#!/usr/bin/env python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_ip = "time.nist.gov"
tcp_port = 13
sock.connect((tcp_ip,tcp_port))
bufsize = 8192

while True:
    data = sock.recv(bufsize)
    if data:
        print (data)
        break
    else:
        print("error")
        break

sock.close()