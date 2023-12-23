# def full_name(fast, last):
#     name = f'full name is: {fast} {last}'
#     return name
# name = full_name(last='kudu',fast='alu')
# print(name)

# def famous_name(first,last, **addition):
#     name = f'{first} {last}'
#     for key, value in addition.items():
#         print(key,value)
#     return name
# name = famous_name(first='king',last='is',title = 'back',title2 = 'ismayel',last2 = 'shekh')
# print(name)
def a_lot(num1,num2):
    sum = num1+num2
    melt = num1 * num2
    remain = num1 - num2
    return sum,melt,remain


everything = a_lot(20, 21)
print(everything)