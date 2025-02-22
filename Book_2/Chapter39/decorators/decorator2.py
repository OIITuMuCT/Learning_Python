# Decorator State Retention Options
class tracer:                       # Состояние через атрибуты экземпляра

    def __init__(self, func):       # При декорировании @
        self.calls = 0              # Сохранить функцию для вызова в будущем
        self.func = func

    def __call__(self, *args, **kwargs):  # При вызове исходной функции
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):                  # To же, что и spam = tracer (spam)
    print(a + b + c)                # Запускается tracer.__ init__


@tracer
def eggs(x, y):                     # To же, что и eggs = tracer (eggs)
    print(x**y)                     # eggs помещается в объект tracer


if __name__ == '__main__':
    spam(1, 2, 3)                   # Вызывается экземпляр tracer:
                                    # запускается tracer.__ call__
    spam(a=4, b=5, c=6)             # spam - атрибут экземпляра
    eggs(2, 16)                     # Вызывается экземпляр tracer, self. func - это eggs
    eggs(4, y=4)                    # self.calls - значение для каждого случая декорирования
