# Check if given number is triangular or not.
from math import sqrt

t=input()
while t>0:
    t-=1
    num=input()
    num*=2
    sq=int(sqrt(num))
    if sq*(sq+1)==num:
        print sq
    else:
        print -1
