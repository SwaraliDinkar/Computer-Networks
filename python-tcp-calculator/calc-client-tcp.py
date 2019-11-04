
import socket		 	
import sys


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 	  		 

try:
    host = "127.0.0.1"   
    port = 8080                      
    s.connect((host, port))                           

    while(True):
        equ=input("Please give me your equation (Ex: 2+2) or Q to quit: ")
        s.send(equ.encode())
        result = s.recv(1024).decode()

        if result == "Quit":
            print("Closing client connection, goodbye")
            break
        elif result == "ZeroDiv":
            print("You can't divide by 0, try again")
        elif result == "MathError":
            print("There is an error with your math, try again")
        elif result == "SyntaxError":
            print("There is a syntax error, please try again")
        elif result == "NameError":
            print("You did not enter an equation, try again")
        else:
            print("The answer is:", result)

    s.close 				

except (IndexError, ValueError):
    print("You did not specify an IP address and port number")
