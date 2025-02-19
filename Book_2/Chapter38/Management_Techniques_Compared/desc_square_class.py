# То же самое, но с помощью дескрипторов (состояние для каждого экземпляра)
class DescSquare(object):
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value

class DescCube(object):
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers(object):
    square = DescSquare()
    cube = DescCube()
    def __init__(self, square, cube):
        self._square = square           # self.square = square тоже работает,
        self._cube = cube               # т.к. приводит к запуску __set__ дескриптора !


if __name__ == '__main__':
    X = Powers(3, 4)
    print(X.square)
    print(X.cube)
    X.square = 5
    print(X.square)
