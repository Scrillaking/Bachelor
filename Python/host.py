
import socket , optparse , os , time
from client import *
from DH import *
from newAES import *

class Host(object):

 def __init__(self , name , ip , port):

	self.ip = ip
	self.port = port
	self.name = name
	self.myID = ''

	self.dh = DiffieHellman()
	self.sessionKey = ''

	self.directory = {}

	self.ipToKey = {}

	self.networkNodes = {
		'10.0.0.1': 2000 , 
		'10.0.0.2': 2100 , 
		'10.0.0.3': 2200 ,

		'10.0.0.20': 3000 , 
		'10.0.0.30': 3000 , 
		'10.0.0.40': 3000
	}
	self.socketIP = ''

	self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	

 def writeToLog(self , text):
	
	with open("log.txt", "a") as myfile:
	 myfile.write("< "+self.name+" >" + "\n" + text + "\n\n")


 def send(self , ip , port , msg):
	if self.socketIP == '':
		self.writeToLog("Initializing socket then Connecting to : " + ip + " : " + str(port))
		self.s.connect((ip, port))
		time.sleep(1)
		self.s.send(str(msg))
		self.writeToLog("sent : " + msg)
		self.socketIP = ip
	elif self.socketIP == ip:
		self.writeToLog("Sending msg as we already have an established socket with : " + ip)
		self.s.send(str(msg))
		self.writeToLog("sent : " + msg)
	else:
		self.writeToLog("Closing socket and opening a new connection with : " + ip)
		self.s.shutdown(socket.SHUT_RDWR)
		self.s.close()
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((ip, port))
		time.sleep(1)
		self.s.send(str(msg))
		self.writeToLog("sent : " + msg)
		self.socketIP = ip

 def receive(self):

	d = self.s.recvfrom(4096)
	if d != '' :
		receivedData = d[0]
		senderAddress = d[1]
		self.writeToLog("Received : "+str(receivedData))
		return str(receivedData)

	

	


 def choosePath(self , dest):

	return ['10.0.0.20' , '10.0.0.30' , '10.0.0.40']   #Will update it later	

 
 def sendData(self , path , data):

	for curIP in reversed(path):
	 aes = AESCipher()
	 data = aes.encrypt(data,self.ipToKey[curIP])
	 self.writeToLog("DATA NOW : "+str(data))

	msg = "DATA" + str(self.nextID(long(self.myID))) + "_" + str(data)
	self.send(path[0] , self.networkNodes[path[0]] , msg)


 def nextID(self , curID):
	return (1 + 4*curID)


 def establishCircuit(self , path , dest):
	
	#Negotiate DH key with the controller
	myPublic = self.dh.genPublicValue()
	self.send(path[0] , self.networkNodes[path[0]] , "CONTROLLERKEY"+str(myPublic))
	time.sleep(0.01)
	response = self.receive()

	info = response.split("_")
	publicValue = info[0]
	self.myID = info[1] 

	self.directory['h3'] = str(self.myID)
	self.sessionKey = self.dh.genSharedSecret(long(publicValue))
	self.writeToLog("SESSION KEY : "+self.sessionKey)

	#Send the path
	time.sleep(0.01)
	aes = AESCipher()

	pathString = ''
	for node in path:
	 pathString += (node+' ')

	time.sleep(0.01)
	encoded = aes.encrypt(pathString,self.sessionKey)
	self.send(path[0] , self.networkNodes[path[0]] , "CONTROLLERPATH"+str(self.myID)+"_"+encoded)
	resp = self.receive()

	#if(resp is "OK"):
	myIDCopy = self.myID

	for curIP in path:
	 self.writeToLog(">>>>>>>>>> "+curIP) 
	 myIDCopy = self.nextID(long(myIDCopy)) 
	 self.send(curIP , self.networkNodes[curIP] , "KEY" + str(myIDCopy) + "_" + str(myPublic))
	 time.sleep(1)
	 reply = self.receive()
	 sharedKey = self.dh.genSharedSecret(long(reply))
	 self.writeToLog("Shared key : "+sharedKey)
	 self.ipToKey[curIP] = sharedKey
	 
	self.writeToLog(str(self.ipToKey))
