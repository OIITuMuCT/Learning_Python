def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Wrapper


@decorator  # C = decorator(C)
class C:
    def __init__(self, x, y):
        self.attr = 'spam'

x = C(6, 7)     # В действительности вызывается Wrapper (6 , 7)
print(x.attr)   # Запускается Wrapper. getattr , выводится spam
