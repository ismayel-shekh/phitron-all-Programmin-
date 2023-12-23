n,x = map(int,input().split())
my_list = list(map(int,input().split()))
for i in range(0,x):
    a,b = map(int,input().split())
    
    toral_sum=0
    for i in range(a-1,b):
        toral_sum += my_list[i]
    print(toral_sum)
