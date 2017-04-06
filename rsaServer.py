# Server code for RSA
import random
import math
import socket
import pickle

def egcd(a,b):
	if a==0:
		return (b,0,1)
	else:
		g,x,y=egcd(b%a,a)
		return (g,y-(b//a)*x,x)
def multiplicative_inverse(a,b):
	g,x,_=egcd(a,b)
	if g==1
		return x%b

def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def isPrime(num):

    if (num < 2):
        return False
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True


    for prime in lowPrimes:
        if (num % prime == 0):
            return False

    return rabinMiller(num)


def generate_random_prime():

	while True:
		num=random.getrandbits(16)
		if isPrime(num):
			return num



p=generate_random_prime()
#print "p: ",p
q=generate_random_prime()
while q==p:
	q=generate_random_prime()

#print "q: ",q
n=p*q
#print "n: ",n
phin=(p-1)*(q-1)
#print "phin ",phin

e=random.randrange(1,phin)

while gcd(e,phin)!=1:
	e=random.randrange(1,phin)

#print "(e,n): ",(e,n)

d=multiplicative_inverse(e,phin)

#print "d: ",d



s=socket.socket()

host=socket.gethostname()

port=12345

s.bind((host,port))

s.listen(5)

while True:
	c,addr=s.accept()
	print 'Got connection from',addr
	c.send("Server: My public parameters are : "+str(e)+" "+str(n))
	cPP=c.recv(4096)   # cPP means client public parameters
	print cPP
	cPP=cPP[34:]
	print cPP
	params=cPP.split()

	cE=int(params[0])  # Client public key
	cN=int(params[1])  # Client
	msg=raw_input("Enter plaintext message to be sent to client: ")
	print msg

	data=[]

	for i in msg:
		val=ord(i)-97
		cval=pow(val,cE,cN)
		data.append(cval)

	data_string=pickle.dumps(data)
	print data_string
	c.send(data_string)
	c.close()

	#cipher=modex(msg,cE,cN)
	#print "Cipher text generated: "
	#print cipher
	#c.send(str(cipher))
	#c.close()
