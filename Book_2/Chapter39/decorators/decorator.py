def decorator(F):
    def wrapper(*args):
        F(*args)
        print(*args)
    return wrapper

@decorator
def func(x, y):
    return print(x + y)

func(6, 7)
