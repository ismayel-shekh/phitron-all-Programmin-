n = int(input())
list =[0,1]
for i in range(2,n):
    x = list[i-1] + list[i-2]
    list.append(x)
print(*list[:n])
# N = int(input())

# fib_sequence = [0, 1]

# for i in range(2, N):
#     next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
#     fib_sequence.append(next_fib)

# print(*fib_sequence[:N])
