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
	serverSocket.close()
	sys.exit()

while True:
	Message,Address = serverSocket.recvfrom(1024)
	
	if(str(Message.decode('utf-8'))=="BYE"):
		serverSocket.close()
		sys.exit()
		
	print("Client: " + str(Message.decode('utf-8')))
	
	Msg = input(">> ")
	serverSocket.sendto(bytearray(Msg,'utf-8'),Address)



