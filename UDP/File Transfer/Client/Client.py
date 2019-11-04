import sys
import socket

IP_ADDRESS="127.0.0.1"
PORT_NUMBER=8080

try:
	clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	print("Socket created succcessfully")
except:
	print("Socket not created")
	sys.exit()

x=input("Enter the file you want:\n")
clientSocket.sendto(x.encode(),(IP_ADDRESS,PORT_NUMBER))

message=(clientSocket.recvfrom(1024))
message1=str(message[0])

f=open('file1.txt',"w")
my_string=message1.encode()
f.write(my_string.decode())
clientSocket.close()

sys.exit()
