# Ceaser Cipher
import math
import random

plain=raw_input("Enter plaintext: ")

shift=int(raw_input("Enter shift amount: "))

cipher=""

for i in plain:
	cipher+=chr(97+(ord(i)-ord('a')+shift)%26)

print "Cipher: ",cipher

decipher=""

for i in cipher:
	decipher+=chr(97+(ord(i)-ord('a')-shift+26)%26)

print "Decipher: "+decipher




