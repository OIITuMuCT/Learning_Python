# powers_class.py

class Powers(object):                       # В Python 2.Х требуется (object)
    """
    Два динамически вычисляемых атрибута, 
    реализованные с помощью свойств
    """
    def __init__(self, square, cube):
        self._square = square              # _square - базовое значение
        self._cube = cube                   # square - имя свойства
    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)

if __name__ == '__main__':
    X = Powers(3, 4)
    print(X.square)
    print(X.cube)
    X.square = 5
    print(X.square)
    # print(X.getSquare())
