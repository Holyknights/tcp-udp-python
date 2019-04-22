from socket import *
import struct
import json
import os
import sys
import time
 
HOST=input("请输入Server IP地址：")
#HOST = "localhost"
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)
wantStop = "Quit"
f1Name = "file1.docx"
f2Name = "file2.docx"
init = "Connected!"
sockCli = socket(AF_INET, SOCK_DGRAM)
sockCli.connect(ADDR)
sockCli.sendto(init.encode('utf-8'),ADDR)

while True:
		data = input(">")
		if (data == wantStop):
			break
		if (data == "file1.docx" or data == "file2.docx" or data == "big.zip"):
					fname = data
					sockCli.sendto(fname.encode('utf-8'),addr)
					count=0
					data = "Transmit mode!"
					fnewname="new"+fname
					f=open(fnewname,'wb')
					while True:
						if count == 0:
							mdata='Yes,I\'m Ready'
							#sockCli.sendto(data.encode('utf-8'),addr)
						mdata,addr = sockCli.recvfrom(BUFSIZE)
						if str(mdata)!="b'end'":
							f.write(mdata)
						else:
							break
						count+=1
					f.close()

		if (data != "Transmit mode!"):
			sockCli.sendto(data.encode('utf-8'),ADDR)
			time.sleep(0.1)
			data, addr = sockCli.recvfrom(BUFSIZE)
			print (data)
 
sockCli.close()
