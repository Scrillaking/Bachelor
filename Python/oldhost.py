#!usr/bin/env python

import socket
import threading
import select
import time
from DH import *
from newAES import *

def main():

   
	class Chat_Client(threading.Thread):
			def __init__(self , name , ip , port):
				threading.Thread.__init__(self)
				self.ip = ip
 				self.port = port
  				self.name = name
  				self.myID = ''
  				self.writeToLog("initialized")

				
				self.running = 1

			def writeToLog(self , text):
  
  				with open("log.txt", "a") as myfile:
  				 myfile.write("< "+self.name+" >" + "\n" + text + "\n\n")


			def choosePath(self , dest):
 				 return ['10.0.0.20' , '10.0.0.30' , '10.0.0.40']

			def nextID(self , curID):
  				return (1 + 4*curID)


			def run(self):
				time.sleep(1)
				self.writeToLog("entered run method ")
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.sock.connect((self.destip, self.PORT))
				f.write("h1 connected to s1 , did s1 change ? " + '\n')               
				time.sleep(0.2)
				self.sock.sendto("I am h1 ",(self.destip, self.PORT))
				f.write("h1 sent data to s1" + '\n')
				f.flush()           
				# Select loop for listen
				while self.running == True:
					#self.sock.send("Hello Server"+"\r\n")
					inputready,outputready,exceptready \
					  = select.select ([self.sock],[self.sock],[])
					for input_item in inputready:
						# Handle sockets
						data = self.sock.recv(1024)
						if data:
							print "Them: " + data
							f = open('log.txt', 'a')
							f.write("h1 received : " + data + '\n')
							f.flush()
						else:
							break
					time.sleep(1)
			def kill(self):
				self.running = 0
				
	
	# Prompt, object instantiation, and threads start here.

	#ip_addr = raw_input('What IP (or type listen)?: ')
	#chat_client.destip = ip_addr
	chat_client = Chat_Client()
	chat_client.start()

if __name__ == "__main__":
	main()



			
