
import socket, optparse, os
from client import *

class Host(object):

 def __init__(self , name , ip , port):

  self.ip = ip
  self.port = port
  self.name = name

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
  self.s.bind((self.ip, self.port))
  

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

 
 def notifyController(self , path):

  self.send(path[0],self.networkNodes[path[0]],"CONTROLLER"+str(path)) 


 def negotiateKeys(self , path):
  
  for curIP in path:

   if curIP in self.networkNodes.keys():
    sharedKey = os.urandom(16) 
    self.ipToKey[curIP] = sharedKey
    self.send(curIP , self.networkNodes[curIP] , sharedKey)

    #otherPublic = self.receive()

  self.writeToLog(str(self.ipToKey))  