# Columnar Transposition
import math
import random
import numpy

plain=raw_input("Enter plaintext: ")
key=raw_input("Enter keyword: ")


colvectors={}

cols=len(key)
rows=int(math.ceil(len(plain)*1.0/cols))

Matrix=[['x' for x in range(cols)] for y in range(rows)]

i=0
j=0

for k in plain:
    if j==cols:
        j=0
        i=i+1
    Matrix[i][j]=k
    j=j+1

print "Plaintext in matrix form: "

for i in range(rows):
    for j in range(cols):
        print Matrix[i][j],
    print

for j in range(cols):
    colvectors[key[j]]=[]
    for i in range(rows):
        colvectors[key[j]].append(Matrix[i][j])

"""
print "Column vectors: "

for i in key:
    print colvectors[i]

"""

# Now I will sort key
sortedKey=''.join(sorted(key))

cipher=""

for i in sortedKey:
    for j in range(rows):
        cipher+=colvectors[i][j]

print "Cipher text is: "

print cipher

decipher=""

cols=len(key)

rows=int(math.ceil(len(cipher)*1.0/cols))

# Lets divide cipher text in column vectors 

colLists=[]

i=0

while i<len(cipher):
    colLists.append(list(cipher[i:i+rows]))
    i+=rows


#print colLists

colVectors={}

for i in range(len(sortedKey)):
    colVectors[sortedKey[i]]=colLists[i]

colLists=[]

for i in range(len(key)):
    colLists.append(colVectors[key[i]])

#print colLists

colVectors=[]

rows=len(colLists[0])
cols=len(colLists)

Matrix2=[['x' for x in range(cols)] for y in range(rows)]

for j in range(len(colLists[0])):
    for i in range(len(colLists)):
        Matrix2[j][i]=colLists[i][j]

print "Deciphered matrix: "

print Matrix2

for i in range(len(Matrix2)):
    for j in range(len(Matrix2[0])):
        decipher+=Matrix2[i][j]

print "Deciphered text: "
print decipher












