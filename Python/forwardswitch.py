import socket
import threading
import time
import optparse, os
from client import *
from DH import *
from newAES import *


class Switch(object):
	def __init__(self , name , ip , port):
		self.ip = ip
		self.port = port
		self.name = name
		self.idToKey = {}
		self.idToNextHob = {}
		self.dh = DiffieHellman()


		self.networkNodes = {
		 '10.0.0.1': 2000 , 
		 '10.0.0.2': 2100 , 
		 '10.0.0.3': 2200 ,

		 '10.0.0.20': 3000 , 
		 '10.0.0.30': 3000 , 
		 '10.0.0.40': 3000
		}
		self.chat_client = Chat_Client(self.name)
		self.chat_client.start()
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.ip, self.port))

		#socket to send data to switch
		self.sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socketIP = ''




	def writeToLog(self , text):
  
	 with open("log.txt", "a") as myfile:
		myfile.write("< "+self.name+" >" + "\n" + text + "\n\n")

	def nextID(self , curID):
		return (1 + 4*curID)

	def replyToHost(self , socket , txt):

		socket.send(txt)



	def sendToSwitch(self , ip , port , msg):
		self.writeToLog('entered sendtoswitch')
		if self.socketIP == '':
			self.writeToLog("Initializing socket then Connecting to : " + ip + " : " + str(port))
			self.sendingSocket.connect((ip, port))
			time.sleep(0.01)
			self.sendingSocket.send(str(msg))
			self.writeToLog("sent : " + msg)
			self.socketIP = ip
		elif self.socketIP == ip:
			self.writeToLog("Sending msg as we already have an established socket with : " + ip)
			self.sendingSocket.send(str(msg))
			self.writeToLog("sent : " + msg)
		else:
			self.writeToLog("Closing socket and opening a new connection with : " + ip)
			self.sendingSocket.shutdown(socket.SHUT_RDWR)
			self.sendingSocket.close()
			self.sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sendingSocket.connect((ip, port))
			time.sleep(0.01)
			self.sendingSocket.send(str(msg))
			self.writeToLog("sent : " + msg)
			self.socketIP = ip

	def listen(self):
		time.sleep(0.01)
		self.sock.listen(5)
		self.writeToLog("Listening for connections")
		while True:
			client, address = self.sock.accept()
			self.writeToLog("Accepted connection from : " + str(address))
			
			time.sleep(0.01)
			client.settimeout(60)
			threading.Thread(target = self.listenToClient,args = (client,address)).start()

	def listenToClient(self, client, address):
		size = 4096
		senderIP = address[0]	
		while True:
			try:
				data = client.recv(size)
				if data:
					receivedData = data
					self.writeToLog("Received :  " + receivedData + "from : " + address[0])


					if receivedData.startswith("CONTROLLER"):
					  response = self.chat_client.sendAndReceive(receivedData[10:])
					  self.writeToLog("sent to controller : " + receivedData[10:])
					  if response:
						self.replyToHost(client,response)
	   
					if receivedData.startswith("KEY"):
						sentMsg = receivedData[3:]
						info = sentMsg.split("_")
						myID = long(info[0])
						otherPublic = long(info[1])
		 
						sharedKey = self.dh.genSharedSecret(otherPublic) 
						self.idToKey[myID] = sharedKey
						self.idToNextHob[myID] = ''
						self.writeToLog("Shared "+sharedKey+" with "+senderIP)

						myPublic = self.dh.genPublicValue()
						self.replyToHost(client , str(myPublic)) 
						self.writeToLog(str(self.idToKey))     

					if receivedData.startswith("DATA"):
						sentMsg = receivedData[4:]
						info = sentMsg.split("_")
						sentID = long(info[0])
						encData = info[1]

						aes = AESCipher()
						decData = aes.decrypt(encData,self.idToKey[sentID])
						self.writeToLog("DEC DATA : "+decData)
						theNextID = self.nextID(long(sentID))

						self.writeToLog("OBTAINING NEXT HOB ....")

						resp = self.chat_client.sendAndReceive("NEXT"+str(theNextID))
						# Got Next hop , now need to establish a new socket between switch and another switch , not the one received from accept because it belongs to the client
						self.writeToLog("NEXT HOB : "+resp)

						msg = "DATA" + str(theNextID) + "_" + str(decData)
						self.sendToSwitch(str(resp) , 3000 , msg)


				else:
					raise error('Client disconnected')
			except:
				client.close()
				return False

