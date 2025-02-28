# Methods MetaClass

class A(type):              # Meтаклаcc (экземпляры=классы)
    def x(cls):
        print('ax', cls)

    def y(cls):             # у переопределяется экземпляром В
        print('ay', cls)


class B(metaclass=A):

    def y(self):            # Нормальный класс
        print('by', self)   # (нормальные экземпляры)

    def z(self):
        print("bz", self)   # Словарь пространств имен хранит у и z


if __name__ == '__main__':
    print(B.x)              # х получается из метакласса
    print(B.y)              # у и z определены в самом классе
    print(B.z)
    B.x()                   # Вызов метода метакласса: получает класс
    I = B()                 # Вызовы методов экземпляра: получают экземпляр
    I.y()
    # I.x()                   # Экземпляр не видит имена метакласса AttributeError
