from socket import *
from time import ctime
import struct
import json
import os
import sys
 
HOST = ""
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)
 
sockSrv = socket(AF_INET, SOCK_DGRAM)
sockSrv.bind(ADDR)

user1 = "2160500040"
user2 = "2160500038"
needUname = "Please enter your user name!"
unameWrong = "You enter a wrong user!"
needPw = "Please enter your password!"
pwWrong = "You enter a wrong password!"
PW = "jsj623840"
connSucc = "Connect sucessfully! We have 2 files, enter file1.docx or file2.docx to get it."
wantStop = "Quit"
rece = "received:"
f1Name = "file1.docx"
f2Name = "file2.docx"
 
while True:
		data, addr = sockSrv.recvfrom(BUFSIZE)
		print ('...connected from:',addr)
		while True:
				data, addr = sockSrv.recvfrom(BUFSIZE)
				print(data)
				if ((data.decode('utf-8') == user1 )or(data.decode('utf-8') == user2)):
					sockSrv.sendto(needPw.encode('utf-8'),addr)
					while True:
						data, addr = sockSrv.recvfrom(BUFSIZE)
						if (data.decode('utf-8') == PW):
							sockSrv.sendto(connSucc.encode('utf-8'),addr)
							while True:
								data, addr = sockSrv.recvfrom(BUFSIZE)
								if (data.decode('utf-8') == wantStop):
									break
								elif (data.decode('utf-8') == 'file1.docx' or data.decode('utf-8') == 'file2.docx' or data.decode('utf-8') == 'big.zip'):
									fname = data.decode('utf-8')
									count=0
									f=open(fname,'rb')
									while True:
										data = f.read(BUFSIZE)
										if str(data)!="b''":
											sockSrv.sendto(data,addr)
										else:
											sockSrv.sendto('end'.encode('utf-8'),addr) #此处文件结束
											break
										count+=1
								else:
									print(data)
									sockSrv.sendto(rece.encode('utf-8'),addr)
						elif (data.decode('utf-8') == wantStop):
							break
						else :
							sockSrv.sendto(pwWrong.encode('utf-8'),addr)
				elif (data.decode('utf-8') == wantStop):
					break
				else :
					sockSrv.sendto(unameWrong.encode('utf-8'),addr)
		sockSrv.close()
 
sockSrv.close()
