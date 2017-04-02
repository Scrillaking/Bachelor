import socket
import threading
import time


class ThreadedServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))

	def listen(self):
		time.sleep(0.01)
		self.sock.listen(5)
		f = open('log.txt','a')
		f.write("listening on s1 for socket " + '\n' )
		f.flush()
		while True:
			client, address = self.sock.accept()
			f.write("s1 accepted someone (changed)  " + '\n' )
			f.flush()
			time.sleep(0.01)
			client.settimeout(60)
			threading.Thread(target = self.listenToClient,args = (client,address)).start()

	def listenToClient(self, client, address):
		size = 1024
		f = open('log.txt','a')
		f.write("s1 got a client  " + '\n' )
		f.flush()
		while True:
			try:
				data = client.recv(size)
				if data:
					response = data
					f.write("s1 received " + response + '\n')
					f.flush()
					time.sleep(0.1)
					client.send("I hear you " + response)


				else:
					raise error('Client disconnected')
			except:
				client.close()
				return False

if __name__ == "__main__":
	ThreadedServer('',5000).listen()