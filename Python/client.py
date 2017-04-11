
import socket , threading , select , time , sys

class Chat_Client(threading.Thread):


 def __init__(self , name):
	threading.Thread.__init__(self)
	self.name = name


 def run(self):
	return

 def writeToLog(self , text):

	with open("log.txt", "a") as myfile:
	 myfile.write("< " + self.name + " >" + "\n" + text + "\n\n")


 def connect(self):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('127.0.0.1',4500))
	return sock


 def sendAndReceive(self, msg):

	msg = msg.replace('\n', ' ').replace('\r', '')
	msg += "\r\n"

	sock = self.connect()
	sock.sendall(msg)
	self.writeToLog('Sent : ' + msg)

	while 1:
	 
	 time.sleep(0.01)
	 response = sock.recv(1024)

	 if not response:
		sock.close()
		break

	 else:
		sock.close()
		self.writeToLog('Controller response : ' + response)
		return response

		#try:
		 
		#except:
		# self.writeToLog("EXCEPTION : "+str(sys.exc_info())) 
			


#client = Chat_Client("SomeName")
#client.sendAndReceive("Hello")
#client.sendAndReceive("Hello again")