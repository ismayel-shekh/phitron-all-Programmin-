# function is a first class object
def double_decker():
    print('srarting the double decker')
    def inner_fun():
        print('inside the decker')
        return 3000
    return inner_fun
# print(double_decker())
# print(double_decker()())
def do_something(work):
    print('coding in python')
    # print(work)
    work()
    print('work starte')
# do_something(2)
# do_something('ami busy')
def coding():
    print('coding in python')
# do_something(coding)
def sleeping():
    print('sleeping and dreming in python')
do_something(sleeping)
