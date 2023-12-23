test = int(input())
count = 0
my_list = list(map(int,input().split()))
while True:
    if all(x %2 ==0 for x in my_list):
        for i in range(test):
            my_list[i] = my_list[i]//2
        count+=1;
    else:
        break

print(count)
# while True:

#     for value in my_list:
        
#         x =int(value)
#         if x % 2 ==0:
#             xcount +=1
            
#         else:
#             break
#     if(xcount == test):
#         count+=1
#         for i in range(len(my_list)):
#             my_list[i]= my_list[i]//2
#         print(my_list)

#     else:
#         break
# print(count)
