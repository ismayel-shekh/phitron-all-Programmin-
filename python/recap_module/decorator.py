# def timer(func):
#     def inner():
#         print('time started')
#         # print(func)
#         func()
#         print("time end")
#     return inner
# # timer()()
# @timer  # if  we simply call to get_fuctorial it works nasted
# def get_fectorial():
#     print('factorial starting')
# get_fectorial()
# # timer(get_fectorial)() # when we not using @timer decarator call that function that way
import math
import time
def timer(func):
    def init(*args,**kwargs):
        start = time.time()
        print("factorial started")
        func(*args,**kwargs)
        print("factorial ended")
        end = time.time()
        print(f'total time taken {end-start}')
    return init
@timer
def get_factorial(n):
    print('factorial starting')
    resust = math.factorial(n)
    print(f'factorial of {n} is : {resust}')
# get_factorial(5)
get_factorial(n=5)

