# Largest product with Given number of Digits

t=input()
while t>0:
    t-=1
    inp = [int(i) for i in raw_input().split()]
    num_inp = [int(i) for i in raw_input()]
    max_prod = 0
    k = inp[0]-inp[1]
    i=0
    while i<=k:
        prod=1
        for j in num_inp[i:i+inp[1]]:
            prod*=j
        if prod>max_prod:
            max_prod=prod
        i+=1
    print max_prod
