
import sys
from host import *
from client import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

h = Host(name , ip , int(port))
path = h.choosePath('h3')

#chat_client = Chat_Client()
#chat_client.start()

h.negotiateKeys(path)