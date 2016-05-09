# Find Largest Prime factor(Timeout for some testcases)
from math import sqrt

t= input()
inp=[]
for i in range(0,t):
    inp.append(input())

def check_prime(n):
    i=2
    sq_rt=int(sqrt(n))
    while i<= sq_rt:
        if n % i == 0:
            return False
        i+=1
    return True

for i in inp:
    j=i/2
    while j>=2:
        if i%j==0 and check_prime(j):
            print j
            break
        j-=1
    if j==1:
        print i
            
    
