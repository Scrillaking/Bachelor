
from random import randint

class DiffieHellman(object):
 

 def __init__(self):
  self.prime = 2**60  
  self.base = 5
  
  self.privateKey = self.genRandom(2)
  self.publicValue = (self.base**self.privateKey) % self.prime


 def genRandom(self, bits):
  range_start = 10**(bits-1)
  range_end = (10**bits)-1
  return randint(range_start, range_end)

 
 def genPublicValue(self):
  return self.publicValue	


 def genSharedSecret(self , otherPublic):
  sessionKey = str((otherPublic ** self.privateKey) % self.prime)
  return sessionKey[0:16] 	



#alice = DiffieHellman()
#bob = DiffieHellman()

#print alice.genSharedSecret(bob.genPublicValue())
#print bob.genSharedSecret(alice.genPublicValue())
