import sys
import socket

IP_ADDRESS="127.0.0.1"
PORT_NUMBER=8080

try:
	clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	print("Socket created successfully")
except:
	print("Socket creation failed")
	sys.exit()


while True:
	msg=input(">>")
	clientSocket.sendto(bytearray(msg.upper(),'utf-8'),(IP_ADDRESS,PORT_NUMBER))

	if(str(msg)=="BYE"):
		clientSocket.close()
		sys.exit()

message=clientSocket.recvfrom(1024)
print("Server : "+message[0].decode('utf-8').strip())

