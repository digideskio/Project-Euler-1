n, k=map(int, raw_input().split())
res=0
def check_pal(num,k):
    if k==2 and bin(num)[2:]== bin(num)[2:][::-1]:
        return True
    elif k==8 and oct(num)[1:]==oct(num)[1:][::-1]:
        return True
    else:
        res=[]
        while num:
            res.append(num%k)
            num/=k
        if res==res[::-1]:
            return True
        return False
        
        
for i in range(1,n):
    if str(i)==str(i)[::-1] and check_pal(i,k):
        res+=i
print res
