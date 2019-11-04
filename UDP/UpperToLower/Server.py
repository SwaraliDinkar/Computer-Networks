import sys
import socket

IP_ADDRESS=""
PORT_NUMBER=8080

try:
	serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	print("Socket created successfully")
except:
	print("Socket creation failed")
	sys.exit()

#socket binding

try:
	serverSocket.bind((IP_ADDRESS,PORT_NUMBER))
	print("Socket binding successful")

except:
	print("Socket binding failed")
	sys.exit()

while True:
	message,address=serverSocket.recvfrom(1024)

	if(str(message.decode('utf-8')=="BYE"))
	serverSocket.close()
	sys.exit()

	print("Client : "+str(message.decode('utf-8')))
	
	msg=input(">>")
	serverSocket.sendto(bytearray((msg.upper(),'utf-8'),address)
