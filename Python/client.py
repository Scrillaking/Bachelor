
import socket
import threading
import select
import time


class Chat_Client(threading.Thread):


 def __init__(self , name):

  threading.Thread.__init__(self)
  self.name = name


 def run(self):
  self.writeToLog('Started')


 def writeToLog(self , text):

  with open("log.txt", "a") as myfile:
   myfile.write("< " + self.name + " >" + "\n" + text + "\n\n")


 def connect(self):

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(('127.0.0.1',4500))
  return sock


 def sendAndReceive(self, msg):

  msg += "\r\n"

  sock = self.connect()
  sock.sendall(msg)
  self.writeToLog('Sent : ' + msg)

  while 1:
   
   response = sock.recv(1024)

   if not response:
    sock.close()
    break

   else:
    self.writeToLog('Controller response : ' + response)
    return response


#client = Chat_Client("SomeName")
#client.sendAndReceive("Hello")
#client.sendAndReceive("Hello again")