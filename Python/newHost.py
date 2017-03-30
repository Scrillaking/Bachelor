
import sys
from host import *
from client import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

h = Host(name , ip , int(port))

h.send('10.0.0.20',3000,"Hello from h1")

#path = h.choosePath('h3')
#h.negotiateKeys(path)