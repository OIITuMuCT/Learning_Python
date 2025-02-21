def decorator(func):
    print('Вычисляется сумма а и б возведенная в квадрат')
    def func(*args):
        a = 5
        b = 10
        return (a + b) ** 2
    print("Результат:")
    return func

@decorator
def func(): ...

print(func())
