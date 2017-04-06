# Author :- Mayank Pratap Singh
# Branch :- IT
import math
import random
import numpy as np

def egcd(a,b):
	if a==0:
		return (b,0,1)
	else:
		g,x,y=egcd(b%a,a)
		return (g,y-(b//a)*x,x)
def multiplicative_inverse(a,b):
	g,x,_=egcd(a,b)
	if g==1:
		return x%b

plain=raw_input("Enter plaintext: ")
mv=[ord(x)-97 for x in plain]
print mv
key=raw_input("Enter key: ")

n=int(math.sqrt(len(key)))

km=[] # key matrix

i=0

while i<len(key):

	var=key[i:i+n]
	var=list(var)
	print var
	var=[ord(x)-97 for x in var]
	km.append(var)
	i=i+n

print km

km=np.matrix(km)
mv=np.matrix(mv).transpose()

print "key matrix: "
print km

print "message vector: "
print mv

cv=km*mv
cv=np.remainder(cv,26)

print "Cipher vector: "
print cv

kinvm=km.I
#print "Regular inverse of key matrix: "
#print kinvm

det=np.linalg.det(km)
#print "Determinant of regular key matrix"
#print det

kmodified=det*kinvm  # Approximation of adjoint matrix
kmodified=np.rint(kmodified)
#print "Adjoint matrix: "
#print kmodified
#print dmv

detinv=multiplicative_inverse(det,26)
#print "Inverse of determinant: ",detinv

kinvm=detinv*kmodified

#print "Inverse matrix:"
#print kinvm

kinvm=np.remainder(kinvm,26)
print "Inverse of key matrix modulo 26: "
print kinvm

decipher=kinvm*cv
#print "Deciphered matrix: "
#print decipher

decipher=np.remainder(decipher,26)
print "Deciphered matrix modulo 26"
print decipher

print "Deciphered text: "

for i in range(len(decipher)):
	for j in range(len(decipher[0])):
		decipher[i][j]=int(decipher[i][j])+97
		print chr(decipher[i][j])

#print decipher
