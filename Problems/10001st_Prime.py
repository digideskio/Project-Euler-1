# Program to find Nth Prime Number
from math import sqrt

t = input()
inp=[]

def check_prime(n):
   """
   checks Primality of a number
   """
   i=2
   sq_rt=int(sqrt(n))
   while i<= sq_rt:
       if n % i == 0:
           return False
       i+=1
   return True

def find_prime(num):
   i = 3
   counter = 1
   while counter < num:
       if check_prime(i):
           res.append(i)
           counter += 1
       i += 2

for i in range(0,t):
    inp.append(input())
res=[2]   
find_prime(max(inp))

for i in inp:
    print res[i-1]
