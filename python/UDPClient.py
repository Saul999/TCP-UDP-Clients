#!/usr/bin/env python3
import socket

UDP_IP = "time.nist.gov"
UDP_PORT = 13
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

sock.bind((UDP_IP, UDP_PORT))
    
while True:
   data, addr = sock.recvfrom(1024) 
   print("received message: %s" % data)

sock.close()