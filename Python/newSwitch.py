
import sys
from forwardswitch import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

#name = "s1"
#ip = "127.0.0.1"
#port = "5000"

s = Switch(name , ip , int(port))
s.listen()