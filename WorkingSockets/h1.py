
import socket, optparse, os

#---------------------------------------    Attributes   -----------------------------------------------
my_IP = "10.0.0.1"
my_Port = 2000

ipToPort = {'10.0.0.20': 3000 , 
            '10.0.0.30': 3100 , 
            '10.0.0.40': 3200
           }  

ipToKey = {'10.0.0.20': '' , 
           '10.0.0.30': '' , 
           '10.0.0.40': ''
          } 

#---------------------------------------    Init   ------------------------------------------------------  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (my_IP, my_Port) )

f = open('h1_log.txt','w')
f.flush()


#---------------------------------------    Talk to switches   ------------------------------------------ 

s1_sessionKey = os.urandom(16)
s2_sessionKey = os.urandom(16)
s3_sessionKey = os.urandom(16)

ipToKey['10.0.0.20'] = str(s1_sessionKey)
ipToKey['10.0.0.30'] = str(s2_sessionKey)
ipToKey['10.0.0.40'] = str(s3_sessionKey)

s.sendto(str(s1_sessionKey), ('10.0.0.20', 3000) )
s.sendto(str(s2_sessionKey), ('10.0.0.30', 3100) )
s.sendto(str(s3_sessionKey), ('10.0.0.40', 3200) )

f.write(str(ipToKey))

f.flush() 