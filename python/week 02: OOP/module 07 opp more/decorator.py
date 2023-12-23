import math
import time
def timer(func):
    def inner(*args,**kwargs):
        print('time started')
        start = time.time()
        # print(func)
        func(*args,**kwargs)
        print('time ended')
        end = time.time()
        print(f'total time token {end - start}')
    return inner
# timer()()
@timer
def get_function(n):
    print('factorial starting')
    Result = math.factorial(n)
    print(f'factorial of {n} is :{Result}')

get_function(1200)