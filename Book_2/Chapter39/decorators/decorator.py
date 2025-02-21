def decorator(F):
    def wrapper(*args):
        x, y = args
        F(*args)
        print(x+y)
    return wrapper

@decorator
def func(x, y):
    print(f'Вычисляем сумму {x} и {y}')

func(6, 7)
