
import socket
import threading
import select
import time

class Chat_Client(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.destip = '127.0.0.1'
        self.sock = None
        self.PORT = 4500
        self.running = 1


    def run(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.destip, self.PORT))
        time.sleep(1)

        while self.running == True:

            inputready,outputready,exceptready = select.select ([self.sock],[self.sock],[])
            for input_item in inputready:
                data = self.sock.recv(1024)
                if data:
                    self.writeToLog("Received : "+data)
                else:
                    break
            time.sleep(1)

    
    def writeToLog(self , text):

        with open("log.txt", "a") as myfile:
            myfile.write("< client >" + "\n" + text + "\n\n")


    def sendToController(self , msg):
        if self.sock is None:
            time.sleep(2)
            self.sock.sendto(msg+"\r\n",(self.destip, self.PORT))
            self.writeToLog("Sent : "+msg+"\r\n")   


    def kill(self):

        self.running = 0