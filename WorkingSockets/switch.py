
import socket, optparse, os
from DiffieHellman import *

class Switch(object):

 def __init__(self , name , ip , port):

  self.ip = ip
  self.port = port
  self.name = name

  self.dh = DiffieHellman()

  self.ipToKey = {
    '10.0.0.1': '' , 
    '10.0.0.2': '' , 
    '10.0.0.3': ''
  }

  self.networkNodes = {
    '10.0.0.1': 2000 , 
    '10.0.0.2': 2100 , 
    '10.0.0.3': 2200 ,

    '10.0.0.20': 3000 , 
    '10.0.0.30': 3100 , 
    '10.0.0.40': 3200
  }

  self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  self.s.bind((self.ip, self.port))

  self.writeToLog("All set")
  self.receive()


 def writeToLog(self , text):
  
  with open("log.txt", "a") as myfile:
   myfile.write("< "+self.name+" >" + "\n" + text + "\n\n")


 def send(self , ip , port , msg):

  self.s.sendto(str(msg), (ip, port))

 
 def receive(self):

  d = self.s.recvfrom(4096)
  receivedData = d[0]
  senderAddress = d[1]
  
  self.writeToLog("Received : "+receivedData)

  if senderAddress[0] in self.ipToKey.keys():
   if(self.ipToKey[senderAddress[0]] == ''):
    self.ipToKey[senderAddress[0]] = self.dh.genKey(receivedData)
    self.send(senderAddress[0] , self.networkNodes[senderAddress[0]] , self.dh.genPublicKey())
    self.writeToLog(str(ipToKey))
   else:
    print "No Match !!" 	

  return receivedData  