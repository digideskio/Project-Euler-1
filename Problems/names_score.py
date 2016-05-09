# Find score of each Query
n=input()
inp=[]
for i in range(0,n):
    inp.append(raw_input())
inp=sorted(inp)

q_num=input()
for i in range(0,q_num):
    quer=raw_input()
    ans=0
    for j in quer:
        ans+=(ord(j)-ord('A')+1)
    ind=inp.index(quer)
    print ans*(ind+1)
