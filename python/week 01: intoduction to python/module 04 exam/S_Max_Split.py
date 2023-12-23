S = input()
L_count = 0
R_count = 0
lists = []
for num in S:
    if num == 'L':
        L_count += 1
    elif num == 'R':
        R_count += 1
    if L_count == R_count:
        lists.append(S[:L_count+R_count])
        S = S[L_count+R_count:]
        L_count = 0
        R_count = 0

# final_list_L = []
# final_list_R = []

# for num in lists:
#     k = "L" * num
#     l = "R" * num
#     final_list_L.append(k)
#     final_list_R.append(l)
# for i in range(len(final_list_L)):
#     final_list_L[i] += final_list_R[i]

print(len(lists))
for num in lists:
    print(num)
