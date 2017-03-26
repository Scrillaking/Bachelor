
import socket
 

#Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 5555))


#Send
msg = 'Hello dear'
s.sendto(msg, ('127.0.0.1', 8888))

#Receive
d = s.recvfrom(4096)
receivedData = d[0]
senderAddress = d[1]
print "127.0.0.1:5555 received : " + receivedData

#Send
msg = 'Hello dear 2'
s.sendto(msg, ('127.0.0.1', 8888))

#Receive
d = s.recvfrom(4096)
receivedData = d[0]
senderAddress = d[1]
print "127.0.0.1:5555 received : " + receivedData