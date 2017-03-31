# Playfair cipher
import math
import random
# Lets make Playfair matrix
plain=raw_input("Enter plaintext: ")
key=raw_input("Enter key for Playfair Cipher: ")
alpha=[]
visited={}
i=0
var=[]
playFairMatrix=[]
while i<len(key):
	if key[i] not in visited:
		visited[key[i]]=1
		if key[i]=='i':
			visited['j']=1
		elif key[i]=='j':
			visited['i']=1
		var.append(key[i])
		i+=1
	else:
		i+=1
for i in range(26):
	if chr(97+i) not in visited:
		var.append(chr(97+i))
var=var[:26]
print(var)

n=5
i=0
while i<len(var):
	tmp=var[i:i+n]
	playFairMatrix.append(tmp)
	i=i+n

print "Playfair Matrix: "
print
print playFairMatrix
i=0
digrams=[]   # List of digrams of plaintext

while i<len(plain):

	tmp=""
	tmp+=plain[i]
	if i+1<len(plain):
		if plain[i+1]==plain[i]:
			tmp+="x"
			i+=1	
		else:
			tmp+=plain[i+1]
			i+=2
	else:
		tmp+="x"
		i+=2
	digrams.append(tmp)
	
print "Plaintext Digrams: "
print(digrams)
address={}
for i in range(5):
	for j in range(5):
		print playFairMatrix[i][j],
		address[playFairMatrix[i][j]]=(i,j)
	print
newdigrams=[]

for pair in digrams:
	add1=address[pair[0]]
	add2=address[pair[1]]
	y1,x1=add1[0],add1[1]
	y2,x2=add2[0],add2[1]

	if y1!=y2 and x1!=x2:
		npair=""
		npair+=playFairMatrix[y1][x2]
		npair+=playFairMatrix[y2][x1]
	elif x1==x2:
		npair=""
		npair+=playFairMatrix[(y1+1)%5][x1]
		npair+=playFairMatrix[(y2+1)%5][x1]
	elif y1==y2:
		npair=""
		npair+=playFairMatrix[y1][(x1+1)%5]
		npair+=playFairMatrix[y1][(x2+1)%5]


	newdigrams.append(npair)
#print newdigrams
decdigrams=[]    # deciphered digrams
# Decryption 

for pair in newdigrams:
	add1=address[pair[0]]
	add2=address[pair[1]]

	y1,x1=add1[0],add1[1]
	y2,x2=add2[0],add2[1]

	if y1!=y2 and x1!=x2:
		npair=""
		npair+=playFairMatrix[y1][x2]
		npair+=playFairMatrix[y2][x1]
	elif x1==x2:
		npair=""
		npair+=playFairMatrix[(y1-1+5)%5][x1]
		npair+=playFairMatrix[(y2-1+5)%5][x1]
	elif y1==y2:
		npair=""
		npair+=playFairMatrix[y1][(x1-1+5)%5]
		npair+=playFairMatrix[y1][(x2-1+5)%5]

	decdigrams.append(npair)

print "Deciphered digrams: "
print decdigrams

print "Deciphered text: "

print ''.join(decdigrams)














