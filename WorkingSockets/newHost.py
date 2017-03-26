
from host import *
from switch import *

h1 = Host('h1' , 'localhost' , 2000)
h1.negotiateKeys(['localhost'])

s1 = switch('s1' , 'localhost' , 3000)
