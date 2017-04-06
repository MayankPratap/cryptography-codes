# Keyed transpose -> Permutation cipher
import math
plain=raw_input("Enter plaintext: ")
cols=int(raw_input("Enter number of columns: "))

key=['x' for x in range(cols)]
keydict={}

print "Enter keys: "

for i in range(cols):
    x=int(raw_input())
    key[i]=x
    keydict[x]=i

rows=int(math.ceil(len(plain)*1.0/cols))

Matrix=[['x' for x in range(cols)] for y in range(rows)]
Matrix2=[['x' for x in range(cols)] for y in range(rows)]

i=0
j=0

for k in plain:
    if j==cols:
        j=0
        i=i+1
    Matrix[i][j]=k
    j=j+1

print "Plaintext in matrix form: "
print Matrix

for i in range(rows):
    for j in range(cols):
        Matrix2[i][j]=Matrix[i][key[j]]

print "Ciphertext in matrix form: "
print Matrix2

Matrix3=[['x' for x in range(cols)] for y in range(rows)]

for i in range(rows):
    for j in range(cols):
        Matrix3[i][j]=Matrix2[i][keydict[j]]

print "Deciphered matrix: "

print Matrix3

decipher=""

for i in range(rows):
    for j in range(cols):
        decipher+=Matrix3[i][j]

print "Deciphered text: "
print decipher
