import random
import math

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
    if (num<2):
        return False

    lowPrimes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59];

    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if (num%prime==0):
            return False
    return rabinMiller(num)



def generate_random_prime():

    while True:
        num=random.getrandbits(16)
        if isPrime(num):
            return num


def choose_primitive_root(p):
    while True:
        alpha=random.randrange(2,p-2)
        visited={}
        #print("alpha ",alpha)
        for i in range(1,p):
            #print(i)
            val=pow(alpha,i,p)
            if val not in visited:
                visited[val]=1
            else:
                break
        if len(visited)==p-1:
            return alpha


# Diffie Hellman Setup

p=generate_random_prime()
print("Modulus: ",p)

alpha=choose_primitive_root(p)

print("Primitive root: ",alpha)

# Diffie Hellman Key exchange

# Alice's parameters
a=random.randrange(2,p-2)  # Private key of Alice
A=pow(alpha,a,p)         # Public key of Alice

# Bob's parameters
b=random.randrange(2,p-2)  # Private key of Alice
B=pow(alpha,b,p)         # Public key of Alice

# Session key

k1=pow(B,a,p)      # Computed by Alice
k2=pow(A,b,p)      # Computed by Bob

if k1==k2:
  print("Shared session key is: ",k1)

else:
  print("Some error in Diffie Hellman algo")
