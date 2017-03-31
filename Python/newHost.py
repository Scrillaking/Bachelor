
import sys
from host import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

h = Host(name , ip , int(port))
path = h.choosePath('h3')

h.writeToLog("1")

myPublic = h.dh.genPublicValue()

h.writeToLog(str(myPublic))

h.send(path[0] , h.networkNodes[path[0]] , "CONTROLLER"+str(myPublic))

#h.notifyController(path)

#h.negotiateKeys(path)