
from Crypto.Cipher import AES
import base64 , os , sys

class AESCipher:

	def __init__( self):
		self.BLOCK_SIZE = 16
		self.PADDING = '\f'
		self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING


	def encrypt( self, message, secret ):
		EncodeAES = lambda c, s: base64.b64encode(c.encrypt(self.pad(s)))
		cipher = AES.new(secret)
		encoded = EncodeAES(cipher, message)
		print 'Encrypted string:>>{}<<'.format(encoded)
		return encoded

	def decrypt( self, encoded , secret ):
		DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(self.PADDING)
		cipher = AES.new(secret)
		decoded = DecodeAES(cipher, encoded)
		print 'Decrypted string:>>{}<<'.format(decoded)
		return decoded