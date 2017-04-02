
import socket
import threading
import select
import time


class Chat_Client(threading.Thread):


 def __init__(self , name):
	threading.Thread.__init__(self)
	self.sock = None # Initialization of the socket is in the sendAndReceive method , which calls the connect function
	self.name = name


 def run(self):
	self.writeToLog('Started')


 def writeToLog(self , text):

	with open("log.txt", "a") as myfile:
	 myfile.write("< " + self.name + " >" + "\n" + text + "\n\n")


 def connect(self):

	self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	self.sock.connect(('127.0.0.1',4500))
	#return sock


 def sendOnly(self, msg):
	msg += "\r\n"
	#sock = self.connect()
	self.sock.sendall(msg)
	self.writeToLog('Sent : ' + msg)




 def sendAndReceive(self, msg):
	msg += "\r\n"

	self.connect()
	self.sock.sendall(msg)
	self.writeToLog('Sent : ' + msg)

	while 1:
	 time.sleep(0.01)
	 response = self.sock.recv(1024)

	 if not response:
		print 'whatever'
		#sock.close()
		#break

	 else:
		self.writeToLog('Controller response : ' + response)
		return response


#client = Chat_Client("SomeName")
#client.sendAndReceive("Hello")
#client.sendAndReceive("Hello again")