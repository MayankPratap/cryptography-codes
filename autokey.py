# Autokey Cipher
import math
import random
# Now I will prepare table 
table={}
table['a']=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(1,26):
	table[chr(97+i)]=table[chr(97+i-1)][1:]
	table[chr(97+i)].extend(table[chr(97+i-1)][0])
plain=raw_input('Enter plaintext: ')
key=raw_input('Enter key: ')
combined=key+plain[:-len(key)]
print(combined)
print(plain)
cipher=""

for i in range(len(combined)):
	cipher+=table[plain[i]][ord(combined[i])-97]
print "Cipher: ",cipher
decipher=""

for i in range(len(key)):
	decipher+=chr((ord(cipher[i])-ord(key[i])+26)%26+97)

dec=decipher

while len(decipher)<len(plain):
	ke=dec
	cip=cipher[len(decipher):]
	dec=""
	for i in range(min(len(ke),len(cip))):
		dec+=chr((ord(cip[i])-ord(ke[i])+26)%26+97)

	decipher+=dec

decipher=decipher[0:len(plain)]
print "Deciphered text: ",decipher
