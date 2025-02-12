# Слоты и словари пространства имен
class C:
    __slots__ = ['a', 'b']

class D:
    __slots__ = ['a', 'b', '__dict__']
    c = 3
    def __init__(self):
        self.d = 4


def main():
    X = C()
    X.a = 1
    print(X.a)
    getattr(X, 'a')
    setattr(X, 'b', 2)
    print(X.b)
    print(X)
    print('Class D:')
    Y = D()
    print(Y.c)
    print(Y.d)
    Y.a = 1
    Y.b = 2
    print(Y.__dict__)

if __name__ == '__main__':
    main()
