t=input()
inp=[input() for i in range(t)]

num=max(inp)
coin=[1,2,5,10,20,50,100,200]

res=[[0 for i in range(8)]for j in range(num+1)]

for i in range(8):
    res[0][i]=1


for i in range(1,num+1):
    for j in range(0,8):
        if i>=coin[j]:
            x=res[i-coin[j]][j]
        else:
            x=0
        if j>0:
            y=res[i][j-1]
        else:
            y=0
        res[i][j]=x+y
for i in inp:
    print res[i][7]%(pow(10,9)+7)
