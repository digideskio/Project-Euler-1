# Doesn't work for Some test cases(Time out)
n=input()
res=0

for i in range(1,n+1):
    res+=pow(i,i)
print res%(pow(10,10))
