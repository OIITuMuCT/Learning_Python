def decorator(F):
    def wrapper(*args):
        x, y = args
        F(x, y)
        print(*args)
        print(x+y)
    return wrapper

@decorator
def func(x, y):
    ...

func(6, 7)
