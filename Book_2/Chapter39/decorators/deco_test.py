def decorator(func):
    print('Вычисляется сумма а и б возведенная в квадрат')
    res = 0
    def func(*args):
        a, b = args
        print( a+b )
        return  f'Result: {sum(a, b)**2}'
    print(f"Результат: {func}")
    return func

@decorator
def func(): ...

func(5, 10)
