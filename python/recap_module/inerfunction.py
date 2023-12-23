def duble_dacker():
    print("hello brothe")
    def iner_fun():
        print("on the way")
        return "alo"
    return iner_fun
# print(duble_dacker()())
def do_something(work):
    print("work started")
    # print(work)
    work()
    print('work end')
# do_something(2)
def coding():
    print("coding in python")
# do_something(coding)
def sleeping():
    print( "king is back")
do_something(sleeping)