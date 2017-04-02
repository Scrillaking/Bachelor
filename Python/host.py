
import socket, optparse, os
from client import *
from DH import *
from AES import *

class Host(object):

 def __init__(self , name , ip , port):

	self.ip = ip
	self.port = port
	self.name = name

	self.dh = DiffieHellman()
	self.sessionKey = ''

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

	self.writeToLog("Received : "+str(receivedData))
	return receivedData


 def choosePath(self):

	return ['10.0.0.20' , '10.0.0.30' , '10.0.0.40']   #Will update it later	

 def pathToString(self, path):

	return path[0] + ":" + path[1] + ":" + path[2] 

 def notifyController(self , path):

	if not self.sessionKey:
	 self.writeToLog("Session key is not yet known")

	else: 
	 cipher = AESCipher('mysecretpassword' , self.sessionKey)
	 encrypted = cipher.encrypt(str(path))
	
	 self.send(path[0],self.networkNodes[path[0]],"CONTROLLER"+encrypted) 


 def negotiateKeys(self , path):
	
	for curIP in path:

	 if curIP in self.networkNodes.keys():
		sharedKey = os.urandom(16) 
		self.ipToKey[curIP] = sharedKey
		self.send(curIP , self.networkNodes[curIP] , sharedKey)

		#otherPublic = self.receive()

		self.writeToLog(str(self.ipToKey))  