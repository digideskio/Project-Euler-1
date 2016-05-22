# sum of Multiples of 3 or 5 below N
test_case=int(raw_input())

for i in range(0,test_case):
    num=input()
    num_3=(num-1)/3
    num_5=(num-1)/5
    num_15=(num-1)/15
    
    sum_3=3*(num_3*(num_3+1)/2)
    sum_5=5*(num_5*(num_5+1)/2)
    sum_15=15*(num_15*(num_15+1)/2)
    
    print sum_3+sum_5-sum_15
    
