test = int(input())
count = 0
my_list = list(map(int,input().split()))
while True:
    if all(x %2 ==0 for x in my_list):
        for i in range(test):
            my_list[i] = my_list[i]//2
        count+=1;
    else:
        break

print(count)