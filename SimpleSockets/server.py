
import socket
 

#create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 3000))


while(1):

 #Receive
 d = s.recvfrom(4096)
 receivedData = d[0]

 if not receivedData: 
  break

 senderAddress = d[1]
 print "Received : " + receivedData

 

 #Send
 #reply = "So, you are saying : "+receivedData
 #s.sendto(reply , senderAddress)
 #print "127.0.0.1:8888 sent : " + reply
     
s.close()