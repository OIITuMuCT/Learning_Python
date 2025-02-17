class E(Exception):
    pass



    
def func1():
    try:
        func2()
    except E:
        print('Print except in func2()')
def func2():
    raise E

try:
    func1()
except E:
    print('Print except block 1 func1()')    