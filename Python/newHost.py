
import sys , time
from host import *
from newAES import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

#name = 'h1'
#ip = '10.0.0.1'
#port = '2000'

h = Host(name , ip , int(port))
path = h.choosePath('h3')

h.establishCircuit(path , 'h3')
h.sendData(path,"Hello World")