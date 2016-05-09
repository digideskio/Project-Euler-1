t=input()

def Find_LCM(a,b):
    if a==1:
        return b
    elif b==1:
        return a
    else:
        if a>b:
            smaller=b
        else:
            smaller=b
        for i in range(1,smaller+1):
            if a%i==0 and b%i==0:
                hcf=i
        return (a*b)/hcf
        
while t>0:
    t-=1
    num=input()
    lcm=1
    for i in range(2,num+1):
        lcm=Find_LCM(lcm,i)
    print lcm
