# x, n = map(int, input().split())
# result = 0
# power = 1
# for i in range(0, n +1 , 2):
#     result += (x ** i)
#     power += 2
# print(result-1)
x,n = map(int,input().split())
result =0
power = 1
for i in range(0,n+1,2):
    result+= (x**i)
print(result-1)