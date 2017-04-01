
import sys , time
from host import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

h = Host(name , ip , int(port))
path = h.choosePath('h3')

myPublic = h.dh.genPublicValue()

time.sleep(1)

h.send(path[0] , h.networkNodes[path[0]] , "CONTROLLERKEY"+str(myPublic))
response = h.receive()

h.writeToLog("SESSION KEY : "+h.dh.genSharedSecret(long(response)))

#h.notifyController(path)

#h.negotiateKeys(path)