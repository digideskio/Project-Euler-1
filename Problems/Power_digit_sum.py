t=input() # number of test cases

while t>0:
    t-=1
    num=pow(2,input())
    res=sum([int(i) for i in str(num)])
    print res
