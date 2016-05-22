# Find Largest Prime factor(Timeout for some testcases)
from math import sqrt

t= input()
inp=[]
for i in range(0,t):
    inp.append(input())


for i in inp:
    if i%2==0:
        largest_prime=2
    else:
        largest_prime=1
    while i%2==0:
        i/=2

    if i==1:
        print largest_prime
    else:
        j=3
        n=sqrt(i)
        while j<=n:
            while i%j==0:
                i/=j
                largest_prime=j
            j+=2
        if i>largest_prime:
            print i
        else:
            print largest_prime

