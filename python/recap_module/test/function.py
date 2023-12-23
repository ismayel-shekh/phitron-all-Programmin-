# # define
# def double_it(num):
#     print('not nessesry')
#     result =num*4
#     return result
# print(double_it(2))

#args
def all_sum(num1,num2,num3,*number):
    print(number)
    sum =0
    for num in number: 
        print(num)
        sum += num
    return sum
total = all_sum (45,46,89,11,81)
print('all sum total ',total)