
import socket, optparse, os
from DiffieHellman import *

class Host(object):

 def __init__(self , name , ip , port):

  self.ip = ip
  self.port = port
  self.name = name

  self.dh = DiffieHellman()

  self.ipToKey = {
    '10.0.0.20': '' , 
    '10.0.0.30': '' , 
    '10.0.0.40': ''
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

  self.writeToLog("Binding ...")
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
  return receivedData


 def choosePath(self , dest):

  return ['10.0.0.20' , '10.0.0.30' , '10.0.0.40']   #Will update it later	


 def negotiateKeys(self , path):
  
  for curIP in path:

   myPublic = self.dh.genPublicKey()
   self.send(curIP , self.networkNodes[curIP] , myPublic)
   self.writeToLog("Sent : "+str(myPublic))

   otherPublic = self.receive()
   self.writeToLog("Received : "+otherPublic)
   shared = self.dh.genKey(otherPublic)
   ipToKey[curIP] = shared
   self.writeToLog(str(ipToKey))