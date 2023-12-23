
n =int(input())
x =0
my_list = list(map(int ,input().split()))
# from collections import Counter
# index_count = Counter(my_list)
index_count ={}
for i in my_list:
   index_count[i] =0
for i in my_list:
   index_count[i] +=1
for val,co in index_count.items():
    if co > val:
      x+=co-val
    elif co < val:
      x+=co

print(x)