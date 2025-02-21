def decorator(F):
    def wrapper(*args):
        # F(*args) # запускает функцию или метод
    return wrapper


@decorator
def func(x, y):             # func = decorator (func)
    ...
    func(6, 7)              # В действительности вызывается wrapper (6, 7)


class C:
    @decorator
    def method(self, x, y):
        ...                 # Повторная привязка к простой функции


X = C()
X.method(6, 7)              # В действительности вызывается wrapper (X, 6, 7)
