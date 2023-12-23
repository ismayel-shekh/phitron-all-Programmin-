# K, S = map(int, input().split())
# count = 0

# for X in range(K + 1):
#     for Y in range(K + 1):
#         Z = S - X - Y
#         print(Z)
#         print(f"{S} '-' {X} '-' {Y}")
#         if 0 <= Z <= K:
#             count += 1

# print(count)
k,s  = map(int,input().split())
count =0
for x in range(k+1):
    for y in range(k+1):
        z = s-x-y
        if 0<=z<=k:
            count+=1
print(count)