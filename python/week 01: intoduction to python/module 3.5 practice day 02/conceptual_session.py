# sampledict = {
#     "class":{
#         "srudent":{
#             "name": "quien",
#             "marks":{
#                 "physics":70,
#                 "history":80
#             }
#         }
#     }
# }
# print(sampledict['class']['srudent']['marks']['history'])
# a = 100
# b = 100
# print(id(a))
# print(id(b))
# split,join
# my_list = list(map(int,input().split()))
# print(my_list)
# lst = [1,2,3,4]
# for i in range(0,len(lst)):
#     lst[i] = lst[i]*lst[i]
# print(*lst)
# def sq(i):
#     return i*i
# result = map(sq,lst)
# print(*lst)
# result = map(lambda i:i*i,lst)
# print(lst)
# x = 10
# y = 20
# if x<y:
#     y,x = x,y
# print(x,y)
a = list(input())
r = " ".join(a)
print(r)
