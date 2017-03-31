# substitution cipher
import math
import random

plain=raw_input("Enter plain text: ")

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

random.shuffle(alpha)

beta={}

for i in range(26):
	beta[alpha[i]]=chr(97+i)

cipher=""

for i in plain:
	cipher+=alpha[ord(i)-97]
	

print "Cipher: ",cipher

decipher=""

for i in cipher:
	decipher+=beta[i]

print "Deciphered: ",decipher
