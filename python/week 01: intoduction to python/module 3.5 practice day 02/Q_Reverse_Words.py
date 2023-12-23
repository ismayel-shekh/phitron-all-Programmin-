s = input()
input_s = s.split()
my_list = []
for word in input_s:
    x = word[::-1]
    my_list.append(x)
print(*my_list)