import sys
import socket

IP_ADDRESS="127.0.0.1"
PORT_NUMBER=8080

try:
	serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	print("Socket created succcessfully")
except:
	print("Socket not created")
	sys.exit()

try:
	serverSocket.bind((IP_ADDRESS,PORT_NUMBER))
	print("Socket binding successful")
except:
	print("Socket binding failed")
	serverSocket.close()
	sys.exit()




message,address=serverSocket.recvfrom(1024)

v=open('file1.txt')
v1=v.read()

try:
	serverSocket.sendto(v1.encode(),address)
except:
	print("Error while reading file")
	sys.exit()
