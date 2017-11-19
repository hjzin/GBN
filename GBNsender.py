#!/usr/bin/env/python3
#-*- coding: utf-8 -*-
#GBN发端
import socket
import threading
import time

#数据总长度
LENGTH=3

#定时器到时时执行的函数
def timeout():
	print('timeout!')
  #停止当前定时器
	timer.cancel()
  
  #如果数据包存在丢失，则重传丢失的包，并设置一个新的定时器
	if end_ack!=LENGTH-1:
		Resend(end_ack)	
		timer1=threading.Timer(5,timeout)
		timer1.start()
    
  #数据包全部发送完成
	else:
		print("数据全部发送成功")

def Resend(endack):
	#发端重传ack
	print('发端重传数据包%d--%d'%(endack+1,LENGTH-1))
	for a in range(endack+1,LENGTH):
		rsendData=bin(a)
		print('发端重传数据%d'%a)
		recvsock.sendto(rsendData.encode('utf-8'),('127.0.0.1',9999))

#设置定时器
timer=threading.Timer(5,timeout)
#创建socket
recvsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#发送数据包
for data in range(start,end):
	sendData=bin(data)
	print('发端发送数据%d'%data)
	recvsock.sendto(sendData.encode('utf-8'),('127.0.0.1',9999))

#启动定时器
timer.start()

while True:
	#接收收端发回的ack
	ack_seq=recvsock.recv(1024)
	print("发端接收ack%d" % int(ack_seq,2))
	end_ack=0
	end_ack=max(end_ack,int(ack_seq,2))






