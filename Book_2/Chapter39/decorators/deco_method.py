class decorator:
    def __init__(self, func):   # func - метод без экземпляра
        self.func = func
    def __call__(self, *args):
        #! self.func(*args) терпит неудачу!
        #! Экземпляр С не находится в args!
class C:
    @decorator
    def method(self, x, y):     # method = decorator(method)
        ...                     # Повторная привязка к экземпляру декоратора