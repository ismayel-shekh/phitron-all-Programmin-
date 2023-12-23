n = int(input())
for _ in range(n):
    x,y =map(int,input().split())
    sum = 0;
    start = min(x,y)+1
    end = max (x,y)
    for i in range(start,end):
        if i%2 == 1:
            sum=sum+i
    print(sum)