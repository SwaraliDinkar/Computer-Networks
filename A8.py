import socket

str=input('Enter the URL:')
type(str)

add=socket.gethostbyname(str)
print('HostName:'+str)
print('IP:'+add)

ip=input('Enter the IP:')
type(ip)

ipadd=socket.gethostbyaddr(ip)

print('IP:'+ip)
print('HostName:'+ipadd[0])

