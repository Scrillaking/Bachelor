
import sys
from host import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

h = Host(name , ip , int(port))

path = h.choosePath('h3')
h.notifyController(path)

#h.negotiateKeys(path)