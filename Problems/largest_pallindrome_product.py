# Largest pallindrome product of 3-digit numbers below N
import bisect

t=input()
res=[]
for i in range(100,999):
    for j in range(i+1,1000):
        prod=i*j
        if str(prod)==str(prod)[::-1]:
                res.append(prod)

res=sorted(res)              
inp=[input()-1 for i in range(t)]
for i in inp:
    ind=bisect.bisect(res,i)
    print res[ind-1]
