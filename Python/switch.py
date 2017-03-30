
import socket, optparse, os
from client import *

class Switch(object):

 def __init__(self , name , ip , port):

  self.ip = ip
  self.port = port
  self.name = name

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

  self.chat_client = Chat_Client()
  self.chat_client.start()
  self.chat_client.sendToController("Hi my name is : "+self.name)
  
  self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  self.s.bind((self.ip, self.port))

  self.listen()


 def writeToLog(self , text):
  
  with open("log.txt", "a") as myfile:
   myfile.write("< "+self.name+" >" + "\n" + text + "\n\n")


 def send(self , ip , port , msg):

  self.s.sendto(str(msg), (ip, port))

 
 def listen(self):

  while(1):
   
   d = self.s.recvfrom(4096)
   receivedData = d[0]
   senderAddress = d[1]
  
   if not receivedData: 
    break

   self.writeToLog("Received : "+receivedData)

   senderIP = senderAddress[0]
   senderPort = int(senderAddress[1])  

   if senderIP in self.ipToKey.keys():

    if(self.ipToKey[senderIP] == ''):

     self.ipToKey[senderIP] = receivedData

     self.writeToLog(str(self.ipToKey))
    
    else:
     self.writeToLog("No match 1")
  
   else:
    self.writeToLog("No match 2") 