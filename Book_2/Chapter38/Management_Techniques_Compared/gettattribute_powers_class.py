# То же самое, но с помощью обобщенного перехвата неопределенных
# атрибутов методом __getattribute__
class Powers(object):
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value)
        else:
            return object.__setattr__(self, name, value)



if __name__ == "__main__":
    X = Powers(3, 4)
    print(X.square)
    print(X.cube)
    X.square = 5
    print(X.square)
