n = int(input())
x = int(n/2)
my_list = list(map(int,input().split()))
flag = True
for i in range(0,x):
    if my_list[i] != my_list[n-i-1]:
        flag=False
        break
if flag :
    print("YES")
else:
    print("NO")
# n = int(input())
# x = n // 2  # Use integer division for the middle index
# my_list = list(map(int, input().split()))
# flag = True

# for i in range(x):
#     if my_list[i] != my_list[n - i - 1]:  # Correct the index here
#         flag = False
#         break

# if flag:
#     print("YES")
# else:
#     print("NO")
