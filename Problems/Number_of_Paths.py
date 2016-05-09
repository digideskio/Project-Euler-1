from math import factorial 

t = input()

while t>0:
    t-=1
    inp = [int(i) for i in raw_input().split()]
    """
    For (m,n), Number of paths are given by
    (m+n)!/m!n!
    Final result is mod of pow(10,9)+7
    """
    print (factorial(inp[0]+inp[1])/(factorial(inp[0])*factorial(inp[1])))%(pow(10,9)+7)
