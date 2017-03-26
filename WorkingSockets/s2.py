
import socket, optparse

#---------------------------------------    Attributes   -----------------------------------------------

my_IP = "10.0.0.30"
my_Port = 3100

ipToPort = {'10.0.0.1': 2000 , 
            '10.0.0.2': 2100 , 
            '10.0.0.3': 2200
           }  

ipToKey = {'10.0.0.1': '' , 
           '10.0.0.2': '' , 
           '10.0.0.3': ''
          } 

#---------------------------------------    Init   ------------------------------------------------------

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (my_IP, my_Port) )

#----------------------------------------   Listen   ----------------------------------------------------

while True:

  sessionKey, addr = s.recvfrom(4096)

  sender_ip = addr[0]

  if sender_ip in ipToKey.keys():    #Authenticated   

   ipToKey[sender_ip] = sessionKey

   with open("s2_log.txt", "a") as myfile:
    myfile.write("S2 ... ")
    myfile.write(str(ipToKey))