# Sum of Primes not grater than N
from math import sqrt

t= input()
inp=[]
res=[0,2]  # initialize reault array

def check_prime(n):
    i=2
    sq_rt=int(sqrt(n))
    while i<= sq_rt:
        if n % i == 0:
            return False
        i+=1
    return True

def find_prime(num):
    i = 3
    counter = 2
    while i <= num:
        if check_prime(i):
            counter += i
        res.append(counter)
        i += 1

for i in range(0,t):
    inp.append(input())
   
find_prime(max(inp))
for i in inp:
    print res[i-1]
