# Управление экземплярами вместо классов

def Tracer(aClass):
    """
    Декоратор для трассировки внешних операций, 
    извлекающих атрибуты экземпляров
    """
    class Wrapper:  # При декорировании @

        def __init__(self, *args, **kwargs):  # При создании экземпляров
            self.wrapped = aClass(
                *args, **kwargs
            )  # Использование имени из объемлющей области видимости
        def __getattr__(self, attrname):
            print("Trace:", attrname)  # Перехват всех атрибутов кроме .wrapped
            return getattr(self.wrapped, attrname)  # Делегирование внутреннему объекту
    return Wrapper

@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
    
bob = Person('Bob', 40, 50)
print(bob.name)
print(bob.pay())
