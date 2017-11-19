#!/usr/bin/env/python3
#-*- coding: utf-8 -*-
#GBN收端
import socket
import random
import time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print("waiting for connection...")
hasrecv=0
while True:
	rcvdata,recvaddress=s.recvfrom(1024)
	seq=int(rcvdata,2)
	#用一个随机数来模拟丢包的情况，丢包概率为0.3
	if random.uniform(0,1)<=0.7:
		#没有丢包，向发端发送ack
		if seq==hasrecv+1:
			hasrecv=hasrecv+1
		print('收端发送ack%d'%hasrecv)
		ackdata=bin(hasrecv)
		s.sendto(ackdata.encode('utf-8'),recvaddress)
	else:
		print('数据包%d丢失！'%seq)
		
		
