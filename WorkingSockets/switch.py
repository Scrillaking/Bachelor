
import socket, optparse, os
from DiffieHellman import *

class Switch(object):

 def __init__(self , name , ip , port):

  self.ip = ip
  self.port = port
  self.name = name

  self.dh = DiffieHellman()

  self.networkNodes = {
    'localhost': 3000 , 
    'localhost': 3100 , 
    'localhost': 3200 ,
    'localhost': 2000 , 
    'localhost': 2100 , 
    'localhost': 2200
  }

  self.ipToKey = {
    'localhost': '' , 
    'localhost': '' , 
    'localhost': ''
  }

  self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  self.s.bind((self.ip, self.port))

  self.writeToLog("All set")


 def writeToLog(self , text):
  
  with open("log.txt", "a") as myfile:
   myfile.write("< "+self.name+" >" + "\n" + text + "\n\n")


 def send(self , ip , port , msg):

  self.s.sendto(str(msg), (ip, port))

 
 def receive(self):

  d = self.s.recvfrom(4096)
  receivedData = d[0]
  senderAddress = d[1]
  
  self.writeToLog("Received : "+receivedData+" From : "+senderAddress[0])

  if senderAddress[0] in self.ipToKey.keys():
   if(self.ipToKey[senderAddress[0]] == ''):
    self.ipToKey[senderAddress[0]] = self.dh.genKey(receivedData)
    self.send(senderAddress[0])
   else:
    print "No Match !!" 	

  return receivedData  