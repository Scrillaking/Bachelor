
import base64 , hashlib , os

from Crypto import Random
from Crypto.Cipher import AES

BS = 32
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AESCipher:

    def __init__( self, key, iv ):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.iv = iv

    def encrypt( self, raw ):
        raw = pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, self.iv )
        return base64.b64encode( self.iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        self.iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        return unpad(cipher.decrypt( enc[16:] ))



#cipher = AESCipher('mysecretpassword' , os.urandom(16))
#encrypted = cipher.encrypt('Hello World')
#decrypted = cipher.decrypt(encrypted)
#print encrypted
#print decrypted