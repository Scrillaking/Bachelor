from newAES import *
aes = AESCipher()
path = aes.choosePath()
pathString = aes.pathToString(path)
key = '1027001405039353'
encoded = aes.encrypt(pathString,key)
decoded = aes.decrypt(encoded,key)