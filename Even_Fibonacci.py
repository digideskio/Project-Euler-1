t=int(raw_input())

while t>0:
    t-=1
    n=int(raw_input())
    inp=[0,1]
    i=1
    sum1=0
    while inp[i]<=n:
        
        inp.append(inp[i]+inp[i-1])
        i+=1
        if inp[i]%2==0:
            sum1+=inp[i]
    if inp[i]%2==0:
        sum1-=inp[i]
    print sum1
