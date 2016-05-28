from math import factorial

n=input()
if n<=19: # for n below 19 answer is 0
    print 0
else:
    res=0
    for i in range(19,n):
        inp=[int(j) for j in str(i)]
        ans=0
        for j in inp:
            ans+=factorial(j)
        if ans%i==0:
            res+=i
    print res
            
