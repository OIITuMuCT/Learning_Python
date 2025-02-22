def deco(func):
    calls = 0
    def inner(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f'call {calls} to {func.__name__}')
        print('Hello', *args, '!!!')
        
    return inner

@deco
def set_name(name):
    pass

set_name('John')
set_name('Bob')


