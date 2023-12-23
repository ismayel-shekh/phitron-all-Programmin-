#lambda
# def double(x):
#     return x*2
double = lambda num: num*2
squared = lambda num: num*num
result = double(44)
output=squared(9)
print(output)
print(result)
add = lambda x,y: x+y
sum=add(11,33)
print(sum)
number = [12,56,98,56,12,6,98]
double_num = map(lambda x: x*2,number)
squared_num = map(lambda x: x*x,number)
print(list(double_num))
print(list(squared_num))
actors = [

    {'name':'sabana','age':65},
    {'name':'sabnoor','age':45},
    {'name':'sabila','age':30},
    {'name':'srabonti','age':38},
    {'name':'shano','age':47},

]
junirs = filter(lambda actor: actor['age'] < 40,actors)
print(list(junirs))
fivers = filter(lambda actor: actor['age'] %5 == 0,actors)
print(list(fivers))