#railfence cipher
import math
plain=raw_input('Enter plaintext: ')
cols=int(raw_input('Enter number of columns: '))

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
    
print "Plaintext in matrix form"

for i in range(rows):
    for j in range(cols):
        print Matrix[i][j],
    print

cipher=""

for i in range(cols):
    for j in range(rows):
        cipher=cipher+Matrix[j][i]
    
print "Ciphertext is : ",cipher

visited={}

decipher=""

for i in range(len(cipher)):
    if i in visited:
        break
    j=i+rows
    flag=0
    decipher=decipher+cipher[i]
    while j<len(cipher):
        if j in visited:
            flag=1
            break
        visited[j]=1
        decipher=decipher+cipher[j]
        j=j+rows
        
    if flag==1:
        break
        
        
        
print "Deciphered text is: ",decipher
