class decorator:
    def __init__(self, func):       # при декорировании @
        self.func = func
    def __call__(self, *args):      # При вызове внутренней функции
        # Использование self.func и аргументов
        # self.func(*args) вызывает исходную функцию

@decorator
def func(x, y):         # func = decorator(func)
    ...                 # func передается__ init__
func(6, 7)              # 6, 7 передается аргументу ★args метода__ call__
