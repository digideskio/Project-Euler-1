# Find the sum of digits of factorial of N

from math import factorial

t=input()
while t>0:
    t-=1
    res=[int(i) for i in str(factorial(input()))] # Extract digits from factorial
    print sum(res)
    
