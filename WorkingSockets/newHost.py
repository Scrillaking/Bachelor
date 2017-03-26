
import sys
from host import *

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

with open("log.txt", "a") as myfile:
 myfile.write("< newHost >" + "\n" + 'Argument List:', str(sys.argv) + "\n\n")

h = Host(name , ip , port)

with open("log.txt", "a") as myfile:
 myfile.write("< newHost >" + "\n" + "Created " + name + "\n\n")

path = h.choosePath('h3')

with open("log.txt", "a") as myfile:
 myfile.write("< newHost >" + "\n" + "Chosen path : " + str(path) + "\n\n")

h.negotiateKeys(path)