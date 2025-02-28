# Управление экземплярами как в предыдущем примере, но с помощью метакласса


def Tracer(classname, supers, classdict):           # При вызове, создающем класс
    aClass = type(classname, supers, classdict)     # Создание клиентского класса

    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = aClass(*args, **kwargs)
        def __getattr__(self, attrname):
            print("Trace:", attrname)  # Перехват всех атрибутов, кроме .wrapped
            return getattr(self.wrapped, attrname) # Делегирование внутреннему объекту
    return Wrapper

class Person(metaclass=Tracer):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate                # Извлечение внутри методов не отслеживается
    def pay(self):
        return self.hours * self.rate

bob = Person("Bob", 40, 50)             # bob - на самом деле экземпляр Wrapper
print(bob.name)                         # Wrapper содержит внедренный экземпляр Person
print(bob.pay())                        # Запускается__ getattr__
print(bob.__class__)

