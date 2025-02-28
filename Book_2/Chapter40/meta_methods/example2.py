# Методы метаклассов или методы классов

class A(type):

    def a(cls):                 # Метод метакласса : получает класс
        cls.x = cls.y + cls.z

class B(metaclass=A):
    y, z = 11, 22
    @classmethod                # Метод класса : получает класс
    def b(cls):
        return cls.x


if __name__ == '__main__':
    print(B.a())
    print(B.x)
    I = B()
    print(I.x, I.y, I.z)
    print(I.b())    # Метод класса: передается класс, не экземпляр;
    # является видимым экземпляру
    print(I.a())    # Методы метакласса: доступны только через класс
