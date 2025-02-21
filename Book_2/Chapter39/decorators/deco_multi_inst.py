# Поддержка множества экземпляров
""" Тем не менее, в отличие от предыдущей показанная
выше версия терпит неудачу при обработке множества экземпляров заданного класса —
каждый вызов, создающий экземпляр, переписывает ранее сохраненный экземпляр. """
class Decorator:
    """ При создании нового экземпляра, старый перезаписывается  """
    def __init__(self, C):  # При декорировании @
        self.C = C

    def __call__(self, *args):  # При создании экземпляров
        self.wrapped = self.C(*args)
        return self

    def __getattr__(self, attrname):  # При извлечении атрибутов
        return getattr(self.wrapped, attrname)


@Decorator  
class C: ...  # C = Decorator(C)


x = C()
y = C()  # Переписывает x!
print(y.__dict__)
y.name = 'John'
print(y.name)
print(y.__dict__)
y.age = 40
print([x for x in y.__dict__.values()])
z = C()
x.name
print(x.name)
print(x.__dict__)
print(y.__dict__)
print(z.__dict__)
print( z == y)
x.addr = '123 main st'
print(z.__dict__)
print(C.__dict__)

