
import sys
from switch import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

s = Switch(name , ip , int(port))