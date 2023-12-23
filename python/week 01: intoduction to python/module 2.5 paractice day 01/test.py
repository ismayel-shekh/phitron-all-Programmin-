# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    x, y = map(int, input().split())
    odd_sum = 0

    if y > x:
        i = x + 1  # Start from x+1 since you want to exclude x
        while i < y:
            if i % 2 == 1:
                odd_sum += i
            i += 1
    else:
        j = y + 1  # Start from y+1 since you want to exclude y
        while j < x:
            if j % 2 == 1:
                odd_sum += j
            j += 1

    print(odd_sum)
