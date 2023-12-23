n = int(input())
for _ in range(n):
    list = []
    s = input()
    for num in s:
        list.append(num)
    list.reverse()
    print(*list)