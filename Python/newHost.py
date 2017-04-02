
import sys , time
from host import *
from newAES import *


name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]
h = Host(name , ip , int(port))
path = h.choosePath()

myPublic = h.dh.genPublicValue()

time.sleep(1)

h.send(path[0] , h.networkNodes[path[0]] , "CONTROLLERKEY"+str(myPublic))
response = h.receive()
sessionKey = h.dh.genSharedSecret(long(response))
h.writeToLog("SESSION KEY : "+ sessionKey)

#Finished Key Exchange , now Send the path encrypted
time.sleep(1)
aes = AESCipher()
pathString = h.pathToString(path)
encoded = aes.encrypt(pathString,sessionKey)
h.send(path[0] , h.networkNodes[path[0]] , "PATH"+encoded)
h.writeToLog("h1 sent " + "PATH" + encoded)



#h.notifyController(path)

#h.negotiateKeys(path)