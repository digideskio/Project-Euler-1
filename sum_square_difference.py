# Program to find Sum square Difference

inp=[]

for i in range(0,input()):
    inp.append(input())

for i in inp:
    print ((i*(i+1)/2)**2)-(i*(i+1)*(2*i+1)/6) 
