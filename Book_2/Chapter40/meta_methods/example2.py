# Методы метаклассов или методы классов

class A(type):

    def a(cls):                 # Метод метакласса : получает класс
        cls.x = cls.y + cls.z

class B(metaclass=A):
    y, z = 11, 22
    @classmethod
    def b(cls):
        return cls.x
