n = input()
my_list = list(map(int,input().split()))
# print(my_list)
m = min(my_list)
mi = my_list.index(m)
x = max(my_list)
xi = my_list.index(x);
my_list[mi] = x
my_list[xi] = m
print(*my_list)