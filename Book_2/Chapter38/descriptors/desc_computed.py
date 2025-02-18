# filename desc_computed.py

class DescSquare:
    """
    Дескриптор,  задействует данные, присоединенные 
    к самому объекту дескриптора(self) 
    """
    def __init__(self, start):
        self._value = start
    def __get__(self, instance, owner):
        return self._value ** 2
    def __set__(self, instance, value):
        self._value = value

class Client1():
    X = DescSquare(3)

class Client2():
    X = DescSquare(32)

c1 = Client1()
c2 = Client2()
print(c1.X)
c1.X = 4
print(c1.X)
print(c2.X)