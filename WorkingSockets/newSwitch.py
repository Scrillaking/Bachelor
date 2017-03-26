
import sys
from switch import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

with open("log.txt", "a") as myfile:
 myfile.write("< newSwitch >" + "\n" + 'Argument List:', str(sys.argv) + "\n\n")

s = Switch(name , ip , port)