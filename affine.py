# Affine Cipher
import math
import random

# Code for extended euclidean algo
def egcd(a,b):
	if a==0:
		return (b,0,1)
	else:
		g,x,y=egcd(b%a,a)
		return (g,y-(b//a)*x,x)
    
# Code for multiplicative inverse using extended euclidean
def mulinv(a,b):
	g,x,_=egcd(a,b)
	if g==1:
		return x%b

plain=raw_input("Enter plaintext: ")
a=int(raw_input("Enter key a: "))
b=int(raw_input("Enter key b: "))

m=26

cipher=[(a*(ord(x)-97)+b)%m for x in plain]
cipher=''.join(chr(i+97) for i in cipher)

print "Cipher text: "
print cipher

ainv=mulinv(a,m)

decipher=[(ainv*((ord(x)-97)-b+m))%m for x in cipher]
decipher=''.join(chr(i+97) for i in decipher)
print "Deciphered message: "
print(decipher)
